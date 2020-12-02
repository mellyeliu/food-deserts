import collections

# population density per square mile of land, -1 represent out of city or negligible 
# each tract is 2.5 miles x 2.5 miles in size

#NOTE: consider expanding each tract into a 3x3 representation in the matrices to have more data points
populationDensityMap = [[-1, -1, 638.63, 800.0, -1, -1, -1, -1, -1, -1, -1], [-1, -1, 949.61, 350.39, -1, -1, -1, -1, -1, -1, -1], [86.66, 367.84, 256.28, 250.39, 219.61, 642.35, 702.94, 307.65, -1, -1, 902.16], [788.82, 165.1, 921.18, 252.55, 261.96, 800.59, 512.55, 882.35, 992.75, 600.19, 629.02], [814.12, 968.24, 1160.39, 503.34, 669.22, 561.76, 567.06, 13.72, 12.75, 6.86, 584.71], [592.55, 1003.14, 1310.78, 586.86, 282.16, 350.39, 383.14, 286.86, 288.82, -1, -1], [216.66, 830.19, 1076.47, 596.86, 898.63, 797.25, 889.61, 525.29, 794.12, -1, -1], [248.63, 434.51, 847.25, 1303.34, 915.29, 824.71, 632.75, 319.22, 543.53, 307.25, -1], [240.19, 171.96, 176.66, 1085.49, 960.78, 1216.86, 1323.14, 2172.55, 639.61, -1, -1], [455.88, 447.25, 644.12, 621.57, 8.63, 7.25, 6.08, 1131.96, 1646.66, -1, -1], [607.65, 473.34, 619.02, 394.51, 8.04, 6.47, 3.34, 864.12, -1, -1, -1], [268.63, 415.29, 576.08, 182.55, 6.66, 4.71, 4.31, -1, -1, -1, -1]]# distanceMap = [[3.66,3.02,3.37,2.02,2.47,1.96,3.82,2.18,3.99,2.47,1.55],

distanceMap = [[1.83, 1.51, 1.69, 1.01, 1.24, 0.98, 1.91, 1.09, 2.0, 1.24, 0.78], [1.96, 1.63, 1.6, 0.94, 0.77, 1.15, 1.05, 1.02, 1.62, 0.93, 0.81], [1.33, 1.17, 1.34, 1.67, 1.81, 1.34, 1.44, 1.98, 1.27, 1.72, 1.52], [1.71, 1.39, 1.41, 1.45, 0.9, 0.79, 1.38, 0.95, 1.82, 1.67, 1.89], [1.09, 1.95, 0.84, 1.96, 1.17, 0.82, 1.25, 1.76, 1.43, 0.96, 1.81], [1.07, 1.76, 1.05, 1.41, 1.02, 1.72, 1.97, 1.02, 1.07, 1.66, 1.94], [1.17, 1.21, 0.82, 1.92, 0.84, 1.71, 1.76, 1.93, 1.95, 1.96, 1.13], [1.36, 1.43, 1.01, 1.38, 1.02, 0.81, 1.01, 1.25, 0.88, 1.44, 1.41], [1.07, 0.94, 1.04, 0.97, 1.63, 1.61, 1.43, 1.26, 1.28, 1.88, 1.02], [1.85, 1.36, 1.77, 1.49, 0.77, 1.12, 1.22, 1.8, 1.18, 1.89, 1.8], [0.78, 1.69, 1.23, 1.18, 1.44, 1.01, 1.7, 1.94, 1.25, 1.76, 1.93], [1.38, 1.99, 1.97, 0.98, 1.7, 1.35, 1.4, 1.03, 1.43, 1.68, 1.73]]

medianHouseholdIncomeMap = [[-1,-1,22829,24336,-1,-1,-1, -1, -1,-1,-1],
[-1,-1,30508,27091,-1,-1,-1, -1, -1, -1,-1],
[25489,16268,30196,51136,26141,54951,60679, 51702, -1,-1,76143],
[24332,17727,28997,46334,22131,31298,42354, 41887, 54776, 61233,64656],
[59460,11234,10545,21347,22424,67321,80517, -1, -1, 62325, 79034],
[82931,11261,21574,23561,75074,76607,112868, 98371, 112432, -1,-1],
[25921,23412,22113,26578,25431,42738,45376,50869, 60732,-1,-1],
[19781,17790,22040,24035,26250,22482,31415,39926,27777,60171,-1],
[29392,41308,37890,27463,29405,32769,31444,24976,40157,-1,-1],
[23059,32995,34556,31593,32455,36742,32413,28342,26754,-1, -1],
[33262,36754,31725,34911,37763,34212,31282,25371, -1, -1,-1],
[45781,26465,64115,45552,37763,36589,36589,-1, -1, -1,-1]]

realEstatePriceMap = [[-1, -1, 95421, 79106, -1, -1, -1, -1, -1, -1, -1], [-1, -1, 88831, 64734, -1, -1, -1, -1, -1, -1, -1], [65687, 64138, 122640, 81879, 86466, 105654, 98273, 150819, -1, -1, 187035], [93613, 79159, 98858, 92392, 96464, 106015, 53644, 97132, 79713, 305782, 391806], [62423, 75832, 45114, 481974, 80482, 87436, 75293, -1, -1, 566859, 535866], [258296, 51088, 92518, 86395, 130017, 173680, 441934, 360295, 450125, -1, -1], [120321, 117962, 60736, 88730, 110230, 89183, 107551, 165307, 133925, -1, -1], [87340, 62853, 108482, 86272, 110105, 68660, 134304, 159414, 96737, 137450, -1], [62825, 105430, 70547, 77557, 63230, 96554, 97190, 106168, 96344, -1, -1], [71866, 56189, 135008, 99699, 135171, 158198, 137117, 139551, 82022, -1, -1], [175360, 12190, 128965, 134306, 142671, 135999, 11900, 133986, -1, -1, -1], [147961, 86648, 173485, 147230, 123343, 144978, 210331, -1, -1, -1, -1]]
count = 0
total_sum = 0

for n in range(len(realEstatePriceMap)):
    for m in range(len(realEstatePriceMap[0])):
        if realEstatePriceMap[n][m] != -1:
            total_sum += realEstatePriceMap[n][m]
            count += 1
            
realEstateAverage = total_sum / count
distanceCap = 8 #12.94
budget = 4000000

def buildingCostBase(locationCost):
  locationCostRatio = locationCost / realEstateAverage
  return locationCostRatio * 25000

def buildingCostSize(size, locationCost):
  locationCostRatio = locationCost / realEstateAverage
  utilityCost = ( 9.17 + 2.61 + 3.59 + 1.81 + 0.93 + 1.43 + 3.85 + 2.76 ) * ( size ) 
  constructionCost = ( 75 * size ) 
  return locationCostRatio * constructionCost + utilityCost

def buildingSize(buildingCost, locationCost):
  locationCostRatio = locationCost / realEstateAverage
  utilities = ( 9.17 + 2.61 + 3.59 + 1.81 + 0.93 + 1.43 + 3.85 + 2.76 )
  construction = 75
  size = buildingCost / (locationCostRatio * construction + utilities)
  
  return size

def storeCapacity(totalSize):
  dailyHours = 12
  tripsPerDay = 7 / 1.6 #7 days divided by 1.6 trips per week
  hoursPerTrip = 43 / 60
  capacityPerPerson = totalSize / 50 
  
  return capacityPerPerson * ( dailyHours / hoursPerTrip ) * tripsPerDay
					# totalSize 1/50 * 12 * 60/43 * 7/1.6 
  				# capacity = totalSize * 1.4651

def storeSize(capacity):
  dailyHours = 12
  tripsPerDay = 7 / 1.6 #7 days divided by 1.6 trips per week
  hoursPerTrip = 43 / 60
  
  return capacity / tripsPerDay / (dailyHours / hoursPerTrip) * 50
  
def capacityToCost(capacity, locationCost):
    return buildingCostSize(storeSize(capacity), locationCost)

def costToCapacity(buildingCost, locationCost):
    return storeCapacity(buildingSize(buildingCost, locationCost))
  
def hasAccess(householdIncome, distance):
  walkingDistance, drivingDistance, lowIncomeThreshold = 0.745, distanceCap, 25000
  walkingScore = 1 if distance < walkingDistance else 0
  carScore = 1 if distance < drivingDistance else 0
  if householdIncome < lowIncomeThreshold:
    return 0.2 * walkingScore + 0.8 * carScore
  return carScore

# key of this is a position tuple (x,y)
# values is a list of tuples (x, y, accessScore) that can access it
locationAccessCache = {}
  
def populationWithAccess(a, b):
  queue = collections.deque([(a, b, 0)])
  visited = set([a, b])
  results = []
  n = len(distanceMap)
  m = len(distanceMap[0])
  while queue: 
    x, y, distanceTravelled = queue.popleft()
    if (x < 0 or y < 0 or x >= n or y >= m):
      continue
    coordinates = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    diagonals = [(x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)]
    currentSize = distanceMap[x][y]
    results.append([x, y, hasAccess(medianHouseholdIncomeMap[x][y], distanceTravelled)])
  	
    for i, j in coordinates:
      if (i < 0 or j < 0 or i >= n or j >= m or (i,j) in visited):
        continue
      straightDistance = currentSize / 2 + distanceMap[i][j] / 2 
      if distanceTravelled + straightDistance <= distanceCap:
        queue.append((i, j, distanceTravelled + straightDistance))
        visited.add((i, j))
    
    for i, j in diagonals:
      if (i < 0 or j < 0 or i >= n or j >= m or (i,j) in visited):
        continue
      diagonalDistance = (2 * ((currentSize / 2) ** 2)) ** 0.5 + (2 * ((distanceMap[i][j] / 2) ** 2)) ** 0.5
      if distanceTravelled + diagonalDistance <= distanceCap:
        queue.append((i, j, distanceTravelled + diagonalDistance))
        visited.add((i, j))
  locationAccessCache[(a,b)] = results
  
def populateCache():
  for i in range(len(populationDensityMap)):
    for j in range(len(populationDensityMap[0])):
      populationWithAccess(i, j)

def findLocationPairs():
  locationPairs = []
  seenPairs = set()
  for locationOne, accessedLocationsOne in locationAccessCache.items():
    for locationTwo, accessedLocationsTwo in locationAccessCache.items():
      if locationOne == locationTwo:
        continue
      if (locationOne, locationTwo) in seenPairs or (locationTwo, locationOne) in seenPairs:
        continue
      seenLocations = set()
      onlyOne, onlyTwo, overlapped = 0, 0, 0
      for accessedLocation in accessedLocationsOne:
        if populationDensityMap[accessedLocation[0]][accessedLocation[1]] == -1:
          continue
        if (accessedLocation[0], accessedLocation[1], 0.8) in accessedLocationsTwo:
          if accessedLocation[2] == 0.8:
            overlapped += populationDensityMap[accessedLocation[0]][accessedLocation[1]] * (distanceMap[accessedLocation[0]][accessedLocation[1]] ** 2)*0.8
          elif accessedLocation[2] == 1:
            overlapped += populationDensityMap[accessedLocation[0]][accessedLocation[1]] * (distanceMap[accessedLocation[0]][accessedLocation[1]] ** 2)*0.8
            onlyOne += populationDensityMap[accessedLocation[0]][accessedLocation[1]] * (distanceMap[accessedLocation[0]][accessedLocation[1]] ** 2)*0.2
        elif (accessedLocation[0], accessedLocation[1], 1) in accessedLocationsTwo:
          if accessedLocation[2] == 0.8: 
            overlapped += populationDensityMap[accessedLocation[0]][accessedLocation[1]] * (distanceMap[accessedLocation[0]][accessedLocation[1]] ** 2)*0.8
            onlyTwo += populationDensityMap[accessedLocation[0]][accessedLocation[1]] * (distanceMap[accessedLocation[0]][accessedLocation[1]] ** 2)*0.2
          elif accessedLocation[2] == 1:
            overlapped += populationDensityMap[accessedLocation[0]][accessedLocation[1]] * (distanceMap[accessedLocation[0]][accessedLocation[1]] ** 2)
        else:
          onlyOne += populationDensityMap[accessedLocation[0]][accessedLocation[1]] * (distanceMap[accessedLocation[0]][accessedLocation[1]] ** 2)*accessedLocation[2]
        seenLocations.add((accessedLocation[0], accessedLocation[1]))
      for accessedLocation in accessedLocationsTwo:
        if populationDensityMap[accessedLocation[0]][accessedLocation[1]] == -1:
          continue
        if (accessedLocation[0], accessedLocation[1]) in seenLocations:
          continue
        onlyTwo += populationDensityMap[accessedLocation[0]][accessedLocation[1]] * (distanceMap[accessedLocation[0]][accessedLocation[1]] ** 2)*accessedLocation[2]
      locationPairs.append((locationOne, locationTwo, onlyOne, onlyTwo, overlapped, onlyOne+onlyTwo+overlapped))
      seenPairs.add((locationOne, locationTwo))
  locationPairs.sort(key = lambda x: x[5], reverse = True)
  return locationPairs
  
  
def findOptimalPair(locationPairs):
  maxAccess = 0
  bestPair = []
  count = 0
  for locationData in locationPairs:
    count += 1
    curAccess = 0
    locationOne, locationTwo, accessOne, accessTwo, overlap, total = locationData
    if maxAccess > total:
        print(count)
        return bestPair, maxAccess
    costA, costB = realEstatePriceMap[locationOne[0]][locationOne[1]], realEstatePriceMap[locationTwo[0]][locationTwo[1]]
    budgetLeft = budget - buildingCostBase(costA) - buildingCostBase(costB)
    if costA < costB:
        accessOne += overlap
        # check cheap location
        if costToCapacity(budgetLeft, costA) > accessOne:
            # enough money
            curAccess += accessOne
            budgetLeft -= capacityToCost(accessOne, costA)
        else:
            # not enough money
            maxAccess = max(costToCapacity(budgetLeft, costA), maxAccess)
            if curAccess == maxAccess: 
                bestPair = [locationOne, locationTwo]
            continue
        # check expensive location
        if costToCapacity(budgetLeft, costB) > accessTwo:
            # enough money
            curAccess += accessTwo
            budgetLeft -= capacityToCost(accessTwo, costB)
        else:
            # not enough money
            curAccess += costToCapacity(budgetLeft, costB)
        maxAccess = max(curAccess, maxAccess)
        if curAccess == maxAccess: 
            bestPair = [locationOne, locationTwo]
    
    else:
      	# check cheap location
        accessTwo += overlap
        if costToCapacity(budgetLeft, costB) > accessTwo:
            # enough money
            curAccess += accessTwo
            budgetLeft -= capacityToCost(accessTwo, costB)
        else:
            # not enough money
            maxAccess = max(costToCapacity(budgetLeft, costB), maxAccess)
            if curAccess == maxAccess: 
                bestPair = [locationOne, locationTwo]
            continue
    		# check expensive location
        if costToCapacity(budgetLeft, costA) > accessOne:
            # enough money
            curAccess += accessOne
            budgetLeft -= capacityToCost(accessOne, costA)
        else:
            curAccess += costToCapacity(budgetLeft, costA)
        maxAccess = max(curAccess, maxAccess)
        if curAccess == maxAccess: 
            bestPair = [locationOne, locationTwo]
  print(count)
  return bestPair, maxAccess
  
def main():
  populateCache()
  locationPairs = findLocationPairs()
  print(len(locationPairs))
  return findOptimalPair(locationPairs)
  
optimalPair, maxAccess = main()
print(optimalPair, maxAccess)