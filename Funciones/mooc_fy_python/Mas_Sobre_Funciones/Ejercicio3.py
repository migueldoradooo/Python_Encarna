def same_chars(text, i, j):
   
    if i < 0 or i >= len(text) or j < 0 or j >= len(text):
        return False

    return text[i] == text[j]

