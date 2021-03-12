from array import array
from GetPath import getRandomPath
from GetPathDistance import getPathDistance
from Greeting import displayGreeting
from GuessAndCheck import guessAndCheck
from LoadMap import loadMap
from Plan import displayPlan
from Greedy import greedy

import time
#https://www.obeythetestinggoat.com/


cityCount = 600
rows, cols = (cityCount, cityCount)
cityMap = [[0 for i in range(cols)] for j in range(rows)]
path =[0 for i in range(cols)]

#displayGreeting()
#displayPlan()
cityMap = loadMap(cityCount)
startTime = time.time()
path = guessAndCheck(path,cityMap)
#getPath(path)
stopTime = time.time()
print("Path:", path)
#distance = getPathDistance(path,cityMap)
#print("Distance:", distance)
print("Time:", (stopTime - startTime))


#greedy(path,cityMap)




#displayGreeting()
#displayPlan()


#guessAndCheck(path,cityMap)
#greedy(path,cityMap)
#bruteForce(path,cityMap)
#noNoseAnt(path,cityMap)
