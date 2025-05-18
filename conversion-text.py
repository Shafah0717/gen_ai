
from translate import Translator

translator = Translator(to_lang='es')
text = "hey whats up boss!"
translation = translator.translate(text)

print("Translated text:", translation)
