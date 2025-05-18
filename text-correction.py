from textblob import TextBlob

text = 'I love progamming and machine learnig.'

blob = TextBlob(text)

corrected = blob.correct()

print(corrected)