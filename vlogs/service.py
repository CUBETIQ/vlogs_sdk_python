import json

import requests
from vlogs.config import BASE_URL
from vlogs.model import CollectorResponse


class VLogsService:
    def __init__(self, base_url=BASE_URL):
        self.url = f"{base_url}/api/v1/collector"

    def post(self, body, headers=None, timeout=None):
        response = requests.post(
            data=json.dumps(body),
            url=self.url,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                **headers,
            },
            timeout=timeout * 1000 if timeout else None,
        )

        if response.status_code in [200, 201, 202]:
            return CollectorResponse(**response.json())
        else:
            raise Exception(
                f"Failed to post data to vlogs server with status code: {response.status_code} and message: {response.text}"
            )
