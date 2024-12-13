def listsum(numList):
    theSum = 0
    for i in numList:
        theSum += i
    return theSum

def listsum2(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum2[1:]

nl = [i for i in range(5)]
print(listsum(nl))
print(listsum2(nl))