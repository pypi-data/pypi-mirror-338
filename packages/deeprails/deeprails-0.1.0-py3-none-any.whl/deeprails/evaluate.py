import requests
from typing import Dict, Any

class EvaluateClient:
    """
    Client for the Evaluate endpoints:
      - POST / (create a new evaluation)
      - GET /{eval_id} (fetch an existing evaluation)
    """
    def __init__(self, base_url: str, headers: Dict[str, str]):
        self.base_url = f"{base_url}/evaluate"
        self.headers = headers

    def create(self, evaluation_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new evaluation by POSTing to /evaluate.
        
        :param evaluation_data: Dict matching the EvaluateCreate model:
            {
              "model_input": {...},
              "model_output": "...",
              "type": "...",
              "guardrails_metrics": [...],
              "score_format": "...",
              "webhook": "..."
            }
        :return: The JSON response from the API as a Python dict
                 matching EvaluationResponse.
        """
        url = self.base_url  # e.g. https://deeprails.ai/evaluate
        response = requests.post(url, json=evaluation_data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch(self, eval_id: str) -> Dict[str, Any]:
        """
        Fetch an existing evaluation by GETting /evaluate/{eval_id}.
        
        :param eval_id: The ID of the evaluation to retrieve
        :return: The JSON response as a Python dict
                 matching EvaluationResponse.
        """
        url = f"{self.base_url}/{eval_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
