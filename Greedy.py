from GetPath import getRandomPath
from GetPathDistance import getPathDistance
import numpy as np
import random
import time

def greedy(path,cityMap):
    #print("\n\nStart of Greedy Algorithm")

    startTime = time.time()
    failToImprove = 0
    print(path)
    noPath = [0 for i in range(len(path))]
    temporaryPath = noPath.copy()

    getRandomPath(temporaryPath)
    shortestDistance = getPathDistance(temporaryPath,cityMap)
    print("Random start, shortest distance:",shortestDistance)
    path = temporaryPath.copy()
    tempDistance = 0
    limitOnTimesToFailToImprove = 1000

    while(failToImprove < limitOnTimesToFailToImprove):
        citiesToVisit = [0 for i in range(len(path))]

        for index in range(len(path)):
            citiesToVisit[index] = index

        temporaryPath = noPath.copy()
        #print("Cities to visit at start",citiesToVisit)

        temporaryPath[0] = pickRandomCity(citiesToVisit)
    
        #print("Place to start:", temporaryPath[0])
        #print("Temp path",temporaryPath)
        #print("Cities to visit after picking random city",citiesToVisit)

        getGreedyPath(temporaryPath,citiesToVisit,cityMap)

        tempDistance =  getPathDistance(temporaryPath,cityMap)
        if(tempDistance < shortestDistance):
            path = temporaryPath.copy()
            shortestDistance = tempDistance
            #print("Shortest distance:",shortestDistance)
        else:
            failToImprove = failToImprove + 1
            #print("Failed to improve.")

    stopTime = time.time()
    print("Greedy Path:", path)
    distance = getPathDistance(path,cityMap)
    print("Greedy Distance:", distance)
    print("Greedy Time:", (stopTime - startTime))

def pickRandomCity(citiesToVisit):
    nextCity = random.choice(citiesToVisit)
    citiesToVisit.remove(nextCity)
    return nextCity

def getGreedyPath(temporaryPath,citiesToVisit,cityMap):
    print("Working Greedy Algorithm (Meat)")
    nearestNeighborMax = np.amax(cityMap)
    for index in range((len(temporaryPath)-1)):
        #print("Where I am:", temporaryPath[index])
        #print("Cities To Visit:", citiesToVisit)
        #print(cityMap)
        nearestNeighbor = nearestNeighborMax
        for checkIndex in range(len(citiesToVisit)):
            nextDistance = cityMap[temporaryPath[index]][citiesToVisit[checkIndex]]
            #print("Next Distance", nextDistance)
            if(nextDistance <= nearestNeighbor):
                nearestNeighbor = nextDistance
                nextCity = citiesToVisit[checkIndex]
        #load the winner from those cities to Visit
        temporaryPath[index+1] = nextCity
        #print("Updated temp path:", temporaryPath)
        #print("We go to:", nextCity)
        citiesToVisit.remove(nextCity)
