from django import forms
from django.utils.safestring import mark_safe
from OctoLingo.translator import OctoLingo

class LanguageSwitcherWidget(forms.Widget):
    template_name = 'octolingo/language_switcher.html'

    def __init__(self, attrs=None, languages=None, current_language='en', with_glossary=False):
        super().__init__(attrs)
        self.languages = languages or [
            ('en', 'English'),
            ('es', 'Spanish'),
            ('fr', 'French'),
            ('de', 'German'),
            ('it', 'Italian'),
            ('pt', 'Portuguese'),
            ('ru', 'Russian'),
            ('zh', 'Chinese'),
            ('ja', 'Japanese'),
            ('ar', 'Arabic')
        ]
        self.current_language = current_language
        self.with_glossary = with_glossary

    def render(self, name, value, attrs=None, renderer=None):
        context = {
            'name': name,
            'languages': self.languages,
            'current_language': value or self.current_language,
            'with_glossary': self.with_glossary
        }
        return mark_safe(renderer.render(self.template_name, context))

    class Media:
        css = {
            'all': ('octolingo/css/octolingo.css',)
        }
        js = ('octolingo/js/octolingo.js',)