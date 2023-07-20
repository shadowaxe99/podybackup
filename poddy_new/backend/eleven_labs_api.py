import requests

class ElevenLabsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.elevenlabs.com"

    def replicate_voice(self, text, voice_id):
        url = f"{self.base_url}/replicate"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "text": text,
            "voice_id": voice_id
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Request failed with status code {response.status_code}")

eleven_labs_api = ElevenLabsAPI("your-api-key")