f = open("./patternCount/dataset_2_10.txt", "r")
# f.readline()
text = f.readline()[:-1]
pattern = f.readline()[:-1]

def patternCount(text, pattern):
    textSize = len(text)
    patternSize = len(pattern)
    count = 0

    for i in range(textSize - patternSize + 1):
        if pattern == text[i:i + patternSize]:
            count = count + 1
    return count

def frequentWords(text, k):
    textSize = len(text)
    count = [0] * (textSize - k + 1)
    frequentPatterns = []
    for i in range(textSize - k + 1):
        count[i] = patternCount(text, text[i:i+k])
    maxCount = max(count)
    for i in range(textSize - k + 1):
        if count[i] == maxCount:
            frequentPatterns.append(text[i:i+k])
    mylist = list(dict.fromkeys(frequentPatterns))
    return mylist

# text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
print (frequentWords(text, 11))

