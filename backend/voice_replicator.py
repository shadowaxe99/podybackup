import requests
from typing import Tuple

class VoiceReplicator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def replicate_voice(self, text: str, voice: str) -> Tuple[bool, str]:
        data = {
            "input": {
                "message": text,
                "voice": voice
            }
        }
        response = requests.post("https://api.eleven-labs.com/v1/voice/replicate", headers=self.headers, json=data)

        if response.status_code == 200:
            return True, response.json()["audio"]
        else:
            return False, response.json()["error"]

    def save_audio(self, audio: str, filename: str) -> None:
        with open(filename, 'wb') as audio_file:
            audio_file.write(audio.encode())
