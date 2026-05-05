def first_word(sentence):
    palabras = sentence.split(" ")
    return palabras[0]

def second_word(sentence):
    palabras = sentence.split(" ")
    return palabras[1]

def last_word(sentence):
    palabras = sentence.split(" ")
    return palabras[-1]


sentence = "it was a dark and stormy python"
print(first_word(sentence))   # it
print(second_word(sentence))  # was
print(last_word(sentence))    # python