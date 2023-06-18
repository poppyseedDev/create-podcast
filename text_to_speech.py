import requests
import json
from dotenv import dotenv_values
from constants import VOICE_STABILITY, VOICE_SIMILARITY_BOOST

class TextToSpeechAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.voice_id = "pz6vzFxT6afcSpv62JCK"  # Replace with the desired voice ID
        self.api_key = dotenv_values(".env.local").get("ELEVEN_LABS_API_KEY")  # Replace with the actual key name

    def convert_text_to_speech(self, text, save_path="audio/audio.mp3"):
        url = f"{self.base_url}/v1/text-to-speech/{self.voice_id}?optimize_streaming_latency=0"  # Replace with the actual URL

        # Request body
        body = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.43,
                "similarity_boost": 0.75
            }
        }

        # Convert the body to JSON format
        json_body = json.dumps(body)

        # Set the headers
        headers = {
            "accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }

        # Send the POST request
        response = requests.post(url, data=json_body, headers=headers)

        # Check the response
        if response.status_code == 200:
            # Successful request
            with open(save_path, 'wb') as audio_file:
                audio_file.write(response.content)
            print("Audio file saved successfully!")
        else:
            # Request failed
            print("Request failed with status code:", response.status_code)
            return None


if __name__ == "__main__":
    # Usage example
    api = TextToSpeechAPI("https://api.elevenlabs.io")  # Replace with the base URL of the API
    response_data = api.convert_text_to_speech("Hello, world!", "audio/audio.mp3")  # Replace with the desired text
    if response_data:
        print(response_data)