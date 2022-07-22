import random, json, sys, os

def readArgs():
    length = 50
    filename = "dict.json"
    startingWord = ""
    numArgs = len(sys.argv) - 1
    if numArgs >= 1: length = int(sys.argv[1])
    if numArgs >= 2: startingWord = sys.argv[2]
    if numArgs >= 3: filename = sys.argv[3]

    return length, filename, startingWord

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
    length, filename, startingWord = readArgs()
    dictionary = loadDict(filename)
    if startingWord == "":
        lastWord = "~" * 15
        result = ""

    else:
        lastWord = startingWord
        result = f"{lastWord} "

    for i in range(0, length):
        newWord = getNextWord(lastWord, dictionary)
        result += f"{newWord} "
        lastWord = newWord

    print(result)

main()
