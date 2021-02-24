from GetPath import getRandomPath
from GetPathDistance import getPathDistance
import time

def guessAndCheck(path,cityMap):
    #print("Start of guess-and-check algorithm.")

    startTime = time.time()
    failToImprove = 0
    tempPath = [0 for i in range(len(path))]

    getRandomPath(tempPath)

    shortestDistance = getPathDistance(tempPath,cityMap)
    #print("G&C First Shortest distance:",shortestDistance)
    path = tempPath.copy()


    tempDistance = 0
    failToImproveLimit = 10000
    while(failToImprove < failToImproveLimit):


        getRandomPath(tempPath)
        tempDistance =  getPathDistance(tempPath,cityMap)

        if(tempDistance < shortestDistance):
            path = tempPath.copy()
            shortestDistance = tempDistance
            print("G&C Shortest distance:",shortestDistance)
        else:
            failToImprove = failToImprove + 1

    stopTime = time.time()
    print("Guess and Check Path:", path)
    distance = getPathDistance(path,cityMap)
    print("Guess and Check Distance:", distance)
    print("Guess and Check Time:", (stopTime - startTime))
    return(path)
