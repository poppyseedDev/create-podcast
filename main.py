import os
from eleven_labs import TextToSpeechAPI
# Assuming the TextToSpeechAPI class is defined as shown in the previous responses

def main():
    api = TextToSpeechAPI("https://api.elevenlabs.io")  # Replace with the base URL of the API

    text = """Long string of text..."""  # Replace with your big string of text

    max_chunk_size = 5000

    # Split the text into chunks of max_chunk_size characters
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]

    for i, chunk in enumerate(chunks):
        save_path = f"audio_{i}.mp3"  # Each result will be saved in a separate file
        api.convert_text_to_speech(chunk, save_path)

if __name__ == "__main__":
    main()
