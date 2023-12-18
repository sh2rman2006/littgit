def getInput():
    return input("-")

def  testInput(n):
    return n.isdigit()

def strToInt(n):
    return int(n)

def printInt(n):
    print(n)

c = getInput()
if testInput(c):
    printInt(strToInt(c))






