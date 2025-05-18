
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sentence = "I am learning ngrams"
tokens = word_tokenize(sentence)

unigram = list(ngrams(tokens,1))
print("unigram:",unigram)

bigram = list(ngrams(tokens,2))
print("bigram:",bigram)

trigram = list(ngrams(tokens,3))
print("trigram:",trigram)