class TranslationError(Exception):
    """Base exception for translation errors."""
    pass

class LanguageNotSupportedError(TranslationError):
    """Exception raised when a language is not supported."""
    pass

class GlossaryError(TranslationError):
    """Exception raised for glossary-related errors."""
    pass

class CacheError(TranslationError):
    """Exception raised for cache-related errors."""
    pass

class HTMLTranslationError(TranslationError):
    """Exception raised for HTML translation errors."""
    pass

class DjangoIntegrationError(TranslationError):
    """Exception raised for Django integration errors."""
    pass