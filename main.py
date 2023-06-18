import os
from text_to_speech import TextToSpeechAPI
from constants import MAX_CHUNK_SIZE

def main():
    # Read the content of the file
    with open("podcast.txt", "r") as file:
        text = file.read()

    api = TextToSpeechAPI("https://api.elevenlabs.io")  # Replace with the base URL of the API

    # Split the text into chunks of max_chunk_size characters
    chunks = [text[i:i + MAX_CHUNK_SIZE] for i in range(0, len(text), MAX_CHUNK_SIZE)]
    
    print("Splitting text into ", len(chunks), " chunks")

    for i, chunk in enumerate(chunks):
        save_path = f"audio/audio_{i}.mp3"  # Each result will be saved in a separate file
        api.convert_text_to_speech(chunk, save_path)

if __name__ == "__main__":
    main()
