import os
from pydub import AudioSegment
from pydub.utils import make_chunks
from create_audio.constants import DURATION_BETWEEN_AUDIO_CHUNKS

class AudioMerger:
    def __init__(self, directory):
        self.directory = directory
        self.merged_audio = AudioSegment.empty()

    def merge_audio_files_with_interval(self):
        # Get a list of all MP3 files in the directory
        audio_files = [file for file in os.listdir(self.directory) if file.endswith(".mp3")]

        if not audio_files:
            print("No MP3 audio files found in the directory.")
            return

        for i, audio_file in enumerate(audio_files):
            file_path = os.path.join(self.directory, audio_file)

            # Load the audio file
            audio = AudioSegment.from_file(file_path, format="mp3")

            # Add DURATION_BETWEEN_AUDIO_CHUNKS-millisecond silence at the end of each audio file (except the last one)
            if i < len(audio_files) - 1:
                silence = AudioSegment.silent(duration=DURATION_BETWEEN_AUDIO_CHUNKS)
                audio += silence

            self.merged_audio += audio

    def export_merged_audio(self, output_file):
        # Export the merged audio to a file
        self.merged_audio.export(output_file, format="mp3")
        print("Merged audio file created:", output_file)

if __name__ == "__main__":
    # Usage example
    directory_path = "audio"  # Replace with the actual directory path

    audio_merger = AudioMerger(directory_path)
    audio_merger.merge_audio_files_with_interval()
    audio_merger.export_merged_audio("merged_audio.mp3")
