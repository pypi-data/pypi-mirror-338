from django.utils.deprecation import MiddlewareMixin
from OctoLingo.translator import OctoLingo
from OctoLingo.glossary import Glossary

class OctoLingoMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.translator = OctoLingo()
        self.glossary = Glossary()

    def process_request(self, request):
        """Set up translation context for the request."""
        # Check if language is set in session or local storage
        user_language = request.session.get('octolingo_language', 'en')
        
        # Check for language change request
        if 'octolingo_language' in request.GET:
            user_language = request.GET['octolingo_language']
            request.session['octolingo_language'] = user_language
        
        # Attach translator and language to request
        request.octolingo = {
            'translator': self.translator,
            'language': user_language,
            'glossary': self.glossary
        }

    def process_response(self, request, response):
        """Optionally translate the response content."""
        if hasattr(request, 'octolingo') and request.octolingo.get('translate_response', False):
            if response.content and 'text/html' in response['Content-Type']:
                try:
                    translated_content, _ = request.octolingo['translator'].translate(
                        response.content.decode('utf-8'),
                        dest_language=request.octolingo['language'],
                        is_html=True
                    )
                    response.content = translated_content.encode('utf-8')
                except Exception as e:
                    # Log error but don't break the response
                    pass
        
        return response