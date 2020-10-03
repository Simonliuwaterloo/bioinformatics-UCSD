def patternMatch(pattern, text):
    indices = []
    textLen = len(text)
    patternLen = len(pattern)
    for i in range(textLen):
        toBeCompare = text[i: i+patternLen]
        if (toBeCompare == pattern):
            indices.append(i)
    return ' '.join(str(v) for v in indices)

f = open('./patternMatching/Vibrio_cholerae.txt', 'r')
pattern = "CTTGATCAT"

text = f.readline()[:-1]
print(patternMatch(pattern, text))