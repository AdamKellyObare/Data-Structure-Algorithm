def word_frequency(sentence):
    # lowercasing and removing punctuations
    # isanlum()  method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.
    sentence = ''.join(e for e in sentence if e.isalnum() or e.isspace()).lower()
    
    # splitting the sentence into words.
    words = sentence.split() 
    
    # calculating frequency of each word.
    frequency = {word: words.count(word) for word in words}
    return frequency

