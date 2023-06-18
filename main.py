from create_audio.main import CreateAudio
from constants import DIR_STORE_AUDIO_CHUNKS, DIR_STORE_FINAL_AUDIO

if __name__ == "__main__":
    converter = CreateAudio(DIR_STORE_AUDIO_CHUNKS, DIR_STORE_FINAL_AUDIO)
    converter.convert_text_to_audio("podcast.txt")