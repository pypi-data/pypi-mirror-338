import os
import json
import requests
from typing import Dict, List, Any, Optional, Union

from .exceptions import (
    PromptOpsError,
    AuthenticationError,
    ResourceNotFoundError,
    ValidationError,
    ServerError,
    RateLimitError
)


class PromptlyzerClient:
    """
    Client for fetching prompts from the Promptlyzer API.
    """
    
    def __init__(
        self,
        api_url: str = None,
        email: str = None,
        password: str = None,
        token: str = None,
        environment: str = "dev"
    ):
        """
        Initialize a new PromptlyzerClient.
        
        Args:
            api_url: The URL of the Promptlyzer API.
            email: The email for authentication.
            password: The password for authentication.
            token: An existing auth token (if available).
            environment: The prompt environment to use (dev, staging, prod).
        """
        self.api_url = api_url or os.environ.get("PROMPTLYZER_API_URL", "http://localhost:8000")
        self.email = email or os.environ.get("PROMPTLYZER_EMAIL")
        self.password = password or os.environ.get("PROMPTLYZER_PASSWORD")
        self.token = token or os.environ.get("PROMPTLYZER_TOKEN")
        self.environment = environment
        
        # If token is not provided but email and password are,
        # authenticate automatically
        if not self.token and self.email and self.password:
            self.authenticate()
    
    def authenticate(self) -> str:
        """
        Authenticate with the Promptlyzer API and get an access token.
        
        Returns:
            str: The access token.
        
        Raises:
            AuthenticationError: If authentication fails.
        """
        if not self.email or not self.password:
            raise AuthenticationError("Email and password must be provided for authentication")
        
        url = f"{self.api_url}/auth/login"
        payload = {
            "email": self.email,
            "password": self.password
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            self.token = data.get("access_token")
            
            if not self.token:
                raise AuthenticationError("No access token returned from server")
            
            return self.token
        
        except requests.HTTPError as e:
            if response.status_code == 401:
                raise AuthenticationError("Invalid email or password") from e
            self._handle_request_error(e, response)
    
    def get_headers(self) -> Dict[str, str]:
        """
        Get the headers for API requests.
        
        Returns:
            Dict[str, str]: The headers with authentication token.
        
        Raises:
            AuthenticationError: If no token is available.
        """
        if not self.token:
            raise AuthenticationError("No authentication token available. Call authenticate() first.")
        
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def list_prompts(self, project_id: str, environment: Optional[str] = None) -> Dict[str, Any]:
        """
        List all prompts in a project.
        
        Args:
            project_id: The ID of the project.
            environment: The environment to filter by. Defaults to client's environment.
            
        Returns:
            Dict[str, Any]: An object containing prompts and total count.
        """
        env = environment or self.environment
        url = f"{self.api_url}/projects/{project_id}/prompts?env={env}"
        headers = self.get_headers()
        
        response = self._make_request("GET", url, headers=headers)
        return response
    
    def get_prompt(self, project_id: str, prompt_name: str, environment: Optional[str] = None) -> Dict[str, Any]:
        """
        Get a specific prompt by name.
        
        Args:
            project_id: The ID of the project.
            prompt_name: The name of the prompt.
            environment: The environment to get the prompt from. Defaults to client's environment.
            
        Returns:
            Dict[str, Any]: The prompt object.
        """
        env = environment or self.environment
        url = f"{self.api_url}/projects/{project_id}/prompts/{prompt_name}?env={env}"
        headers = self.get_headers()
        
        response = self._make_request("GET", url, headers=headers)
        return response
    
    def list_prompt_versions(self, project_id: str, prompt_name: str, environment: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List all versions of a prompt.
        
        Args:
            project_id: The ID of the project.
            prompt_name: The name of the prompt.
            environment: The environment to get versions from. Defaults to client's environment.
            
        Returns:
            List[Dict[str, Any]]: A list of version objects.
        """
        env = environment or self.environment
        url = f"{self.api_url}/projects/{project_id}/prompts/{prompt_name}/versions?env={env}"
        headers = self.get_headers()
        
        response = self._make_request("GET", url, headers=headers)
        return response
    
    def _make_request(self, method: str, url: str, headers: Dict[str, str] = None, json_data: Dict[str, Any] = None) -> Any:
        """
        Make a request to the Promptlyzer API.
        
        Args:
            method: The HTTP method to use.
            url: The URL to request.
            headers: The headers to include.
            json_data: The JSON data to send.
            
        Returns:
            Any: The parsed JSON response.
            
        Raises:
            Various PromptOpsError subclasses depending on the error.
        """
        try:
            response = requests.request(method, url, headers=headers, json=json_data)
            response.raise_for_status()
            return response.json()
        
        except requests.HTTPError as e:
            return self._handle_request_error(e, response)
    
    def _handle_request_error(self, error: requests.HTTPError, response: requests.Response) -> None:
        """
        Handle HTTP errors from the API.
        
        Args:
            error: The HTTPError exception.
            response: The response object.
            
        Raises:
            AuthenticationError: For 401 status codes.
            ResourceNotFoundError: For 404 status codes.
            ValidationError: For 400 and 422 status codes.
            RateLimitError: For 429 status codes.
            ServerError: For 500+ status codes.
            PromptOpsError: For all other error codes.
        """
        status_code = response.status_code
        
        try:
            error_data = response.json()
            detail = error_data.get("detail", "Unknown error")
        except (ValueError, KeyError):
            detail = response.text or "Unknown error"
        
        if status_code == 401:
            raise AuthenticationError(detail, status_code, response)
        elif status_code == 404:
            raise ResourceNotFoundError(detail, status_code, response)
        elif status_code in (400, 422):
            raise ValidationError(detail, status_code, response)
        elif status_code == 429:
            raise RateLimitError(detail, status_code, response)
        elif status_code >= 500:
            raise ServerError(detail, status_code, response)
        else:
            raise PromptOpsError(detail, status_code, response)