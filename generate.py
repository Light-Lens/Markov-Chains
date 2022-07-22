import random, json, sys, os

def readArgs():
    length = 50
    filename = "dict.json"
    numArgs = len(sys.argv) - 1
    if numArgs >= 1: length = int(sys.argv[1])
    if numArgs >= 2: filename = sys.argv[2]

    return length, filename

def loadDict(filename):
    if not os.path.exists(filename): sys.exit("Error: Dict.json not found")
    with open(filename, "r") as File: dictionary = json.load(File)
    return dictionary

def pickRandom(dict):
    randNum = random.randint(0, len(dict)-1)
    newWord = list(dict.keys())[randNum]
    return newWord

def getNextWord(lastWord, dict):
    if lastWord not in dict:
        newWord = pickRandom(dict)
        return newWord

    else:
        candidates = dict[lastWord]
        candidatesNormalized = []
        for word in candidates:
            freq = candidates[word]
            for i in range(0, freq): candidatesNormalized.append(word)

        rnd = random.randint(0, len(candidatesNormalized)-1)
        return candidatesNormalized[rnd]

def main():
    length, filename = readArgs()
    dictionary = loadDict(filename)
    lastWord = "~" * 15
    result = ""
    for i in range(0, length):
        newWord = getNextWord(lastWord, dictionary)
        result += f" {newWord}"
        lastWord = newWord

    print(result)

main()
