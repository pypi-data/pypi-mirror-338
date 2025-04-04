import argparse
import json
import os
import sys
from typing import Dict, Any, List, Optional

from .client import PromptlyzerClient
from .exceptions import PromptOpsError
from .utils import prettify_json


def create_parser() -> argparse.ArgumentParser:
    """Create the command line argument parser."""
    parser = argparse.ArgumentParser(
        description="Promptlyzer CLI - Manage and analyze prompts from the command line"
    )
    
    # Global options
    parser.add_argument(
        "--api-url", 
        help="Promptlyzer API URL. Can also be set via PROMPTLYZER_API_URL env variable."
    )
    parser.add_argument(
        "--email", 
        help="Email for authentication. Can also be set via PROMPTLYZER_EMAIL env variable."
    )
    parser.add_argument(
        "--password", 
        help="Password for authentication. Can also be set via PROMPTLYZER_PASSWORD env variable."
    )
    parser.add_argument(
        "--token", 
        help="Auth token. Can also be set via PROMPTLYZER_TOKEN env variable."
    )
    parser.add_argument(
        "--env", 
        choices=["dev", "staging", "prod"],
        default="dev",
        help="Environment (dev, staging, prod). Default: dev"
    )
    
    # Create subparsers for commands
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # List prompts command
    list_parser = subparsers.add_parser("list", help="List prompts in a project")
    list_parser.add_argument("project_id", help="Project ID")
    
    # Get prompt command
    get_parser = subparsers.add_parser("get", help="Get a specific prompt")
    get_parser.add_argument("project_id", help="Project ID")
    get_parser.add_argument("prompt_name", help="Prompt name")
    
    # List versions command
    versions_parser = subparsers.add_parser("versions", help="List prompt versions")
    versions_parser.add_argument("project_id", help="Project ID")
    versions_parser.add_argument("prompt_name", help="Prompt name")
    
    return parser


def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        client = PromptlyzerClient(
            api_url=args.api_url,
            email=args.email,
            password=args.password,
            token=args.token,
            environment=args.env
        )
        
        if args.command == "list":
            result = client.list_prompts(args.project_id)
            print(prettify_json(result))
        
        elif args.command == "get":
            result = client.get_prompt(args.project_id, args.prompt_name)
            print(prettify_json(result))
        
        elif args.command == "versions":
            result = client.list_prompt_versions(args.project_id, args.prompt_name)
            print(prettify_json(result))
        
    except PromptOpsError as e:
        print(f"Error: {e.message}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()