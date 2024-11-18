import os

def ensure_directory(path):
    """Ensure a directory exists, create if it doesn't"""
    if not os.path.exists(path):
        os.makedirs(path)

def clean_text(text):
    """Clean and preprocess text"""
    return text.strip() 