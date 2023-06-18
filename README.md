# Text-to-Speech Converter

This repository contains a Python script that converts a long text into speech by utilizing a Eleven Labs API. The script breaks down the input text into smaller chunks and saves each resulting speech segment in a separate audio file. After that these files are merged together.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/poppyseedDev/create-podcast
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain an API key

   - Acquire an API key from Eleven Labs.
   - Copy the `env.local.example` into `.env.local`
   - Add the API key to the `.env.local` file:

     ```plaintext
     API_KEY=your-api-key
     ```

4. Prepare the input text:

   - Place the long text to be converted into the `podcast.txt` file.

5. Run the script:

   ```bash
   python main.py
   ```

6. Check the generated audio files:

   - The script will create separate audio files for each text chunk in the `audio_#.wav` format.

## TODO:
### For making audio work:
- [x] calling Eleven Labs API
- [x] test chunking 5000 characters
- [x] take all audio files and merge them together

### For making automated podcast generation work
- look into autoGPT how it works and implement a specific funtionality of iterating until the desired podcast text is done

## Configuration

- Adjust the `MAX_CHUNK_SIZE` constant in the `constants.py` file to modify the maximum chunk size for text segmentation.

## License

This project is licensed under the [MIT License](LICENSE).
```
