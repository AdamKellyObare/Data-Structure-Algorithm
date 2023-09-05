import re

def word_frequency(sentence):
    words = re.sub("[^\w]", " ",  sentence.lower()).split()
    frequencies = {word: words.count(word) for word in words}
    return frequencies

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

