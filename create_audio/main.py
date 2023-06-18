from create_audio.text_to_speech import TextToSpeechAPI
from create_audio.constants import MAX_CHUNK_SIZE
from create_audio.split_text_into_chunks import TextSplitter
from create_audio.merge_audio_files import AudioMerger

class CreateAudio:
    """
    A class for converting text to audio by splitting it into chunks, converting each chunk to speech,
    and then merging the resulting audio files.
    """
    def __init__(self, dir_store_audio_chunks, dir_store_final_audio):
        """
        Initializes a CreateAudio instance.
        """
        self.api = TextToSpeechAPI("https://api.elevenlabs.io")
        self.dir_store_audio_chunks = dir_store_audio_chunks
        self.dir_store_final_audio = dir_store_final_audio

    def split_into_chunks(self, text, display=False):
        """
        Splits the given text into smaller chunks.

        Args:
            text (str): The text to split into chunks.
            display (bool, optional): Whether to display the chunks and their lengths. Defaults to False.

        Returns:
            list: A list of text chunks.
        """
        splitter = TextSplitter(MAX_CHUNK_SIZE)
        chunks = splitter.split_text(text)

        print("Splitting text into", len(chunks), "chunks")

        if display:
            for i, chunk in enumerate(chunks):
                print(f"Chunk {i+1} (Length: {len(chunk)}):\n{chunk}\n{'-' * 50}\n")

        return chunks

    def go_through_chunks(self, chunks):
        """
        Converts each chunk of text to speech.

        Args:
            chunks (list): A list of text chunks.
        """
        for i, chunk in enumerate(chunks):
            save_path = self.dir_store_audio_chunks + f"/audio_{i}.mp3"
            self.api.convert_text_to_speech(chunk, save_path)

    def merge_audio_files(self, directory_path, output_file):
        """
        Merges audio files from a directory into a single audio file.

        Args:
            directory_path (str): The path to the directory containing audio files.
            output_file (str): The path to the output merged audio file.
        """
        audio_merger = AudioMerger(directory_path)
        audio_merger.merge_audio_files_with_interval()
        audio_merger.export_merged_audio(output_file)

    def convert_text_to_audio(self, text_file_path):
        """
        Converts the text from a file to audio by splitting it into chunks, converting each chunk to speech,
        and then merging the resulting audio files.

        Args:
            text_file_path (str): The path to the text file.
        """
        with open(text_file_path, "r") as file:
            text = file.read()

        chunks = self.split_into_chunks(text, display=True)
        self.go_through_chunks(chunks)
        self.merge_audio_files(self.dir_store_audio_chunks, self.dir_store_final_audio + "/merged_audio.mp3")

if __name__ == "__main__":
    converter = CreateAudio()
    converter.convert_text_to_audio("podcast.txt")
