class TextSplitter:
    """
    A class used to split text into chunks.

    ...

    Attributes
    ----------
    max_chunk_size : int
        the maximum size for each chunk of text

    Methods
    -------
    split_text(text: str) -> list:
        Splits the text into chunks of maximum size max_chunk_size, 
        trying to split on paragraph boundaries where possible.
    """

    def __init__(self, max_chunk_size=500):
        """
        Constructs all the necessary attributes for the TextSplitter object.

        Parameters
        ----------
        max_chunk_size : int
            the maximum size for each chunk of text (default is 500)
        """
        self.max_chunk_size = max_chunk_size

    def split_text(self, text):
        """
        Splits the text into chunks of maximum size max_chunk_size, 
        trying to split on paragraph boundaries where possible.

        Parameters
        ----------
        text : str
            long string to be split into chunks

        Returns
        -------
        list
            a list of strings, each string is a chunk of the original text
        """
        chunks = []
        current_chunk = ""
        for paragraph in text.split("\n"):
            if len(current_chunk) + len(paragraph) < self.max_chunk_size:
                current_chunk += paragraph + "\n"
            else:
                # If the paragraph is huge and more than max_chunk_size
                while len(paragraph) >= self.max_chunk_size:
                    current_chunk += paragraph[:self.max_chunk_size]
                    paragraph = paragraph[self.max_chunk_size:]
                    chunks.append(current_chunk)
                    current_chunk = ""

                current_chunk += paragraph + "\n"
                chunks.append(current_chunk)
                current_chunk = ""

        if current_chunk:  # Any leftover text smaller than max_chunk_size
            chunks.append(current_chunk)

        return chunks
