import requests
from typing import Dict, Any

class MonitorClient:
    """
    Client for the Monitor endpoints:
      - POST / (create a new monitor)
      - POST /{monitor_id}/event (log an event)
    """
    def __init__(self, base_url: str, headers: Dict[str, str]):
        self.base_url = f"{base_url}/monitor"
        self.headers = headers

    def create(self, monitor_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new monitor.
        
        :param monitor_data: Dict matching the MonitorCreate model:
            {
              "name": "...",
              "description": "...",
              "metrics": [...]
            }
        :return: Dictionary with e.g. {"monitor_id": "..."} from the API.
        """
        url = self.base_url  # e.g. https://deeprails.ai/monitor
        response = requests.post(url, json=monitor_data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def log(self, monitor_id: str, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Log an event under a specific monitor.
        
        :param monitor_id: ID of the monitor to which we log the event
        :param event_data: Dict matching MonitorEventCreate:
            {
              "model_input": {...},
              "model_output": {...},
              "temperature": 0.7,
              "top_p": 1.0,
              "model": "gpt-3.5-turbo",
              ...
            }
        :return: Dictionary with e.g. {"event_id": "..."} from the API.
        """
        url = f"{self.base_url}/{monitor_id}/event"
        response = requests.post(url, json=event_data, headers=self.headers)
        response.raise_for_status()
        return response.json()
