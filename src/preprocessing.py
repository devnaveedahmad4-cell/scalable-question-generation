import fitz
from pathlib import Path


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
            print(f"✅ Loaded PDF: {file.name} ({len(doc)} pages)")
        
        elif file.suffix.lower() == ".txt":
            text = file.read_text(encoding="utf-8", errors="ignore")
            documents.append(text)
            print(f"Loaded TXT: {file.name} ({len(text)} chars)")
        
        else:
            print(f"Skipping unsupported file: {file.name}")

    return documents