import json
from typing import Dict, Any, Union


def prettify_json(obj: Union[Dict, list]) -> str:
    """
    Format a JSON object for nice display.
    
    Args:
        obj: The object to format.
        
    Returns:
        str: Formatted JSON string.
    """
    return json.dumps(obj, indent=2)