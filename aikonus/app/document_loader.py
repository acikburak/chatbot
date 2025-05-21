import os
import sys

# Belgeler ana dizinden okunacağı için yol ayarlaması
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCUMENTS_DIR = os.path.join(BASE_DIR, "documents")

def load_documents(documents_path=DOCUMENTS_DIR):
    full_text = ""

    for filename in os.listdir(documents_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(documents_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
                    full_text += f"\n[DOKUMAN: {filename}]\n{file_content}\n"
            except Exception as e:
                print(f"[HATA] {filename} dosyasi okunamadi: {e}")

    return full_text.strip()
