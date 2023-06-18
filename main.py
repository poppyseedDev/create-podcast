import os
from text_to_speech import TextToSpeechAPI
from constants import MAX_CHUNK_SIZE
from split_text_into_chunks import TextSplitter

def split_into_chunks(text, display=False):
    splitter = TextSplitter(MAX_CHUNK_SIZE)
    chunks = splitter.split_text(text)
    
    print("Splitting text into ", len(chunks), " chunks")

    # Print the chunks and their lengths
    if display:
        for i, chunk in enumerate(chunks):
            print(f"Chunk {i+1} (Length: {len(chunk)}):\n{chunk}\n{'-'*50}\n")

    return chunks

def go_through_chunks(api, chunks):
    for i, chunk in enumerate(chunks):
        save_path = f"audio/audio_{i}.mp3"  # Each result will be saved in a separate file
        api.convert_text_to_speech(chunk, save_path)

def main():
    # Read the content of the file
    with open("podcast.txt", "r") as file:
        text = file.read()

    api = TextToSpeechAPI("https://api.elevenlabs.io")  # Replace with the base URL of the API
    
    split_into_chunks(text, display=True)

    #go_through_chunks(api, chunks)

if __name__ == "__main__":
    main()
