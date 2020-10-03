COML_MAP = {
    "A": "T",
    "C": "G",
    "G": "C",
    "T": "A"
}

def reverseComplement(text):
    empty = ""
    for i in reversed(range(len(text))):
        empty += COML_MAP[text[i]]
    return empty

f = open('./reverseComplement/dataset_3_2.txt', 'r')
inString = f.readline()[:-1]
print(reverseComplement(inString))