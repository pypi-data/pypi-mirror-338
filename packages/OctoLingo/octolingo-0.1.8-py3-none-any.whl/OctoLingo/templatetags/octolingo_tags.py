from django import template
from django.utils.safestring import mark_safe
from OctoLingo.utils import save_to_local_storage, load_from_local_storage

register = template.Library()

@register.simple_tag
def octolingo_language_switcher(current_language='en', with_glossary=False):
    """Render the language switcher dropdown."""
    languages = [
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
    
    options = ''.join(
        f'<option value="{code}" {"selected" if code == current_language else ""}>{name}</option>'
        for code, name in languages
    )
    
    glossary_html = '''
    <div class="glossary-section" style="margin-top: 10px; display: none;">
        <h4>Custom Glossary</h4>
        <textarea id="octolingo-glossary" placeholder="Enter glossary terms (one per line in format: term=translation)"></textarea>
        <button onclick="applyGlossary()">Apply Glossary</button>
    </div>
    ''' if with_glossary else ''
    
    html = f'''
    <div class="octolingo-language-switcher">
        <select id="octolingo-language-select" onchange="changeLanguage(this.value)">
            {options}
        </select>
        {glossary_html}
    </div>
    {save_to_local_storage('octolingo_language', current_language)}
    '''
    
    return mark_safe(html)

@register.filter
def translate_text(text, language):
    """Template filter to translate text."""
    # This is a placeholder - actual translation would need access to the translator
    # In practice, this would use the translator from the request context
    return f"{text} (translated to {language})"