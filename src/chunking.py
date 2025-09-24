import re
from typing import List


def chunk_documents(documents, max_tokens=500, overlap=50) -> List:
    
    all_chunks = []

    for doc in documents:
        words = re.split(r"\s+", doc)
        start = 0
        while start < len(words):
            end = start + max_tokens
            chunk = words[start: end]
            all_chunks.append(chunk)
            start = start + max_tokens - overlap

    return all_chunks