import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize

sample_text = 'I love Programming'
tokens = word_tokenize(sample_text)

print(tokens)