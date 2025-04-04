import requests
from typing import Dict, Any

from .evaluate import EvaluateClient
from .monitor import MonitorClient

class DeepRails:
    """
    Main entry point for the deeprails client.
    
    Usage:
        from deeprails import DeepRails
        
        client = DeepRails(token="YOUR_TOKEN")
        resp = client.evaluate.create({...})
    """
    def __init__(self, token: str, base_url: str = "https://deeprails.ai"):
        """
        :param token: Bearer token for authentication.
        :param base_url: Base URL for the DeepRails API.
        """
        self.token = token
        self.base_url = base_url.rstrip("/")
        # Common headers for all requests
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        # Create client objects
        self.evaluate = EvaluateClient(self.base_url, self.headers)
        self.monitor = MonitorClient(self.base_url, self.headers)
