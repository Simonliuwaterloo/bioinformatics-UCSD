def findClumps(L, t, k, text):
    freqMap = {}
    length = len(text)
    ret = []
    #setup
    first = text[0:k] #first word in sliding window
    last = text[L-k:L] #last word in sliding window
    for i in range(L):
        currWord = text[i:i+k]
        if currWord in freqMap:
            freqMap[currWord] += 1
        else:
            freqMap[currWord] = 1
    for key, value in freqMap.items():
        if value >= t:
            ret.append(key)
    for windowStartIndex in range(1, length - L):
        freqMap[first] -= 1
        first = first[1:] + text[windowStartIndex+k-1]
        last = last[1:]+text[windowStartIndex+L-1]
        if last in freqMap:
            freqMap[last] += 1
        else:
            freqMap[last] = 1
        if freqMap[last] >= t:
            ret.append(last)
    ret = list(dict.fromkeys(ret))
    return ' '.join(ret)

f = open('./findClumps/dataset_4_5.txt', 'r')
text = f.readline()[:-1]

k = 8
L = 24
t = 3
print(findClumps(L, t, k, text))

