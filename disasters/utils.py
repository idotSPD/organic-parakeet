from googletrans import Translator, LANGUAGES

def translate_text(text, target_language='fr'):
    """
    Translate text to the target language using Google Translate API.
    :param text: The text to translate (in English).
    :param target_language: The target language code (default is 'fr' for French).
    :return: Translated text in the target language.
    """
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text
