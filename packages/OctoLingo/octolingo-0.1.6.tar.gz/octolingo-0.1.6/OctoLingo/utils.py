import re
import hashlib
from functools import wraps
import json
import os

def split_text_into_chunks(text, max_chunk_size=4900):
    """Split the text into chunks, ensuring sentences are not broken."""
    sentences = re.split(r'(?<=[.!?]) +', text)  # Split by sentence boundaries
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) > max_chunk_size:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence
        else:
            current_chunk += " " + sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def cache_translation(func):
    """Decorator to cache translations."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Generate cache key based on all relevant arguments
        text = args[1] if len(args) > 1 else kwargs.get('text', '')
        dest_language = args[2] if len(args) > 2 else kwargs.get('dest_language', '')
        src_language = args[3] if len(args) > 3 else kwargs.get('src_language', 'auto')
        is_html = args[5] if len(args) > 5 else kwargs.get('is_html', False)
        
        cache_key = hashlib.md5(
            f"{text}_{dest_language}_{src_language}_{is_html}".encode('utf-8')
        ).hexdigest()

        # Check cache
        if cache_key in wrapper.cache:
            return wrapper.cache[cache_key]

        # Call the function and cache the result
        result = func(*args, **kwargs)
        wrapper.cache[cache_key] = result
        return result

    wrapper.cache = {}  # Initialize cache
    return wrapper

def save_to_local_storage(key, value):
    """Save data to browser's local storage (for client-side use)."""
    return f"""
    <script>
        localStorage.setItem('{key}', '{json.dumps(value)}');
    </script>
    """

def load_from_local_storage(key, default=None):
    """Load data from browser's local storage (for client-side use)."""
    return f"""
    <script>
        var value = localStorage.getItem('{key}');
        if (value) {{
            document.write(value);
        }} else {{
            document.write('{json.dumps(default)}');
        }}
    </script>
    """