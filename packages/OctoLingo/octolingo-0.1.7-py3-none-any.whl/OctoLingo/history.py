import json
import os
from datetime import datetime
from OctoLingo.exceptions import TranslationError

class TranslationHistory:
    def __init__(self, history_file='translation_history.json'):
        self.history_file = history_file
        self._initialize_history_file()

    def _initialize_history_file(self):
        """Initialize the history file if it doesn't exist."""
        if not os.path.exists(self.history_file):
            with open(self.history_file, 'w') as f:
                json.dump([], f)

    def log_translation(self, source_text, translated_text, src_language, dest_language, metadata=None):
        """Log a translation to the history."""
        try:
            with open(self.history_file, 'r+') as f:
                history = json.load(f)
                entry = {
                    'timestamp': datetime.now().isoformat(),
                    'source_text': source_text,
                    'translated_text': translated_text,
                    'src_language': src_language,
                    'dest_language': dest_language,
                    'metadata': metadata or {}
                }
                history.append(entry)
                f.seek(0)
                json.dump(history, f, indent=4)
        except Exception as e:
            raise TranslationError(f"Failed to log translation: {str(e)}")

    def get_history(self, limit=None, filter_by=None):
        """Retrieve the translation history with optional filtering and limiting."""
        try:
            with open(self.history_file, 'r') as f:
                history = json.load(f)
                
                # Apply filters if provided
                if filter_by:
                    history = [entry for entry in history if all(
                        entry.get(key) == value for key, value in filter_by.items()
                    )]
                
                # Apply limit if provided
                if limit is not None and limit > 0:
                    history = history[-limit:]
                
                return history
        except Exception as e:
            raise TranslationError(f"Failed to retrieve history: {str(e)}")

    def clear_history(self):
        """Clear the translation history."""
        try:
            with open(self.history_file, 'w') as f:
                json.dump([], f)
        except Exception as e:
            raise TranslationError(f"Failed to clear history: {str(e)}")