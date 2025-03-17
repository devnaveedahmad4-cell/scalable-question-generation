from pyPDF2 import PdfReader
from pathlib import Path

def load_docs(data_dir: Path, stream_pdf: bool = True):
    documents = list()

    for file in sorted(data_dir.iterdir()):
        reader = PdfReader(file)

        if file.suffix.lower() == ".pdf":
            if stream_pdf:
                for i, page in enumerate(reader.pages):
                    page_text = page.extract_text()
                    if page_text and page_text.strip():
                        documents.append(page_text)

                print(f"Loaded PDF (streaming): {file.name} with {len(reader.pages)} pages")

        elif file.suffix.lower() == ".txt":
            text = ""
            for page in reader:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            documents.append(text)
            
            print(f"Loaded PDF (full): {file.name} ({len(text)} chars)")
        else:
            print(f"Skipped unsupported file type: {file.name}")
