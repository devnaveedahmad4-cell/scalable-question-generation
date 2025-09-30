import fitz
from pathlib import Path
import re
from typing import List

def load_docs(data_dir: Path, stream_pdf: bool = True):
    documents = list()

    for file in sorted(data_dir.iterdir()):
        if file.suffix.lower() == ".pdf":
            doc = fitz.open(file)
            text = ""
            for page_num in range(len(doc)):
                page = doc[page_num]
                text += page.get_text("text") + "\n"
            documents.append(text)
            print(f"Loaded PDF: {file.name} ({len(doc)} pages)")
        elif file.suffix.lower() == ".txt":
            text = file.read_text(encoding="utf-8", errors="ignore")
            documents.append(text)
            print(f"Loaded TXT: {file.name} ({len(text)} chars)")
        else:
            print(f"Skipping unsupported file: {file.name}")

    return documents

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