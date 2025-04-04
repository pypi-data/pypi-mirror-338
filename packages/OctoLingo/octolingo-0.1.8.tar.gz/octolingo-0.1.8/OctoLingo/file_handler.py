import os
import json
from OctoLingo.exceptions import TranslationError

class FileHandler:
    @staticmethod
    def read_file(file_path, encoding='utf-8', fallback_encodings=['latin-1', 'utf-16', 'cp1252']):
        """Read text from a file with automatic encoding detection and fallback."""
        for enc in [encoding] + fallback_encodings:
            try:
                with open(file_path, 'r', encoding=enc) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
        raise UnicodeDecodeError(f"Could not decode {file_path} with any of the provided encodings")

    @staticmethod
    def write_file(file_path, content, encoding='utf-8', errors='replace'):
        """Write text to a file with specified encoding and error handling."""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding=encoding, errors=errors) as f:
            f.write(content)

    @staticmethod
    def save_translation_cache(cache, file_path='translation_cache.json'):
        """Save translation cache to a file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(cache, f)
        except Exception as e:
            raise TranslationError(f"Failed to save cache: {str(e)}")

    @staticmethod
    def load_translation_cache(file_path='translation_cache.json'):
        """Load translation cache from a file."""
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            raise TranslationError(f"Failed to load cache: {str(e)}")