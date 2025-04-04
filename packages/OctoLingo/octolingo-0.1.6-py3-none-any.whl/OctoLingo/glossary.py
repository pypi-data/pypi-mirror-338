import re
from OctoLingo.exceptions import TranslationError
import json

class Glossary:
    def __init__(self, file_path=None):
        """Initialize glossary, optionally loading from a file."""
        self.glossary = {}
        if file_path:
            self.load_from_file(file_path)

    def add_term(self, term, translation):
        """Add a custom term and its translation to the glossary."""
        self.glossary[term] = translation

    def remove_term(self, term):
        """Remove a term from the glossary."""
        if term in self.glossary:
            del self.glossary[term]

    def apply_glossary(self, text):
        """Apply the glossary to the text."""
        if not self.glossary:
            return text
            
        # Sort terms by length (longest first) to handle multi-word terms correctly
        sorted_terms = sorted(self.glossary.keys(), key=len, reverse=True)
        
        for term in sorted_terms:
            # Use regex to match whole words only
            pattern = re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)
            text = pattern.sub(self.glossary[term], text)
        
        return text

    def load_from_file(self, file_path):
        """Load glossary terms from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.glossary.update(data)
        except Exception as e:
            raise TranslationError(f"Failed to load glossary: {str(e)}")

    def save_to_file(self, file_path):
        """Save glossary terms to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.glossary, f, indent=4)
        except Exception as e:
            raise TranslationError(f"Failed to save glossary: {str(e)}")

    def clear(self):
        """Clear all glossary terms."""
        self.glossary = {}