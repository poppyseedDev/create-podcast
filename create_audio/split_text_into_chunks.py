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

    def __init__(self, max_chunk_size=5000):
        self.max_chunk_size = max_chunk_size

    def split_text(self, text):
        chunks = []
        current_chunk = ""
        
        # Check if there are paragraph breaks
        if '\n\n' in text:
            units = text.split('\n\n')
        elif '\n' in text:
            units = text.split('\n')
            
        for unit in units:
            if len(current_chunk) + len(unit) < self.max_chunk_size:
                current_chunk += unit + "\n\n"
            else:
                # If the unit is huge and more than max_chunk_size
                while len(unit) >= self.max_chunk_size:
                    current_chunk += unit[:self.max_chunk_size]
                    unit = unit[self.max_chunk_size:]
                    chunks.append(current_chunk)
                    current_chunk = ""

                current_chunk += unit + "\n"
                chunks.append(current_chunk)
                current_chunk = ""

        if current_chunk:  # Any leftover text smaller than max_chunk_size
            chunks.append(current_chunk)

        return chunks
