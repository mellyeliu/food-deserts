import collections

# population density per square mile of land, -1 represent out of city or negligible 
# each tract is 2.5 miles x 2.5 miles in size

#NOTE: consider expanding each tract into a 3x3 representation in the matrices to have more data points
populationDensityMap = [[-1,-1,3257,4080,-1,-1,-1, -1, -1,-1,-1],
[-1	,		-1,	4843,	1787,		-1,		-1,		-1, 	-1, 	-1, 	-1,		-1],
[442,	1876,	1307,	1277,	1120,	3276,	3585,	1569, 	-1,		-1,	4601],
[4023,	842,4698,1288,1336,4083,2614, 4500, 5063, 3061,3208],
[4152,4938,5918,2567,3413,2865,2892, 70, 65,35, 2982],
[3022,5116,6685,2993,1439,1787,1954, 1463, 1473, -1,-1],
[1105,4234,5490,3044,4583,4066,4537, 2679, 4050,-1,-1],
[1268,2216,4321,6647,4668,4206,3227, 1628, 2772,1567,-1],
[1225,877,901,5536,4900,6206,6748,11080, 3262, -1,-1],
[2325,2281,3285,3170,44,37,31,5773,8398, -1, -1],
[3099,2414,3157,2012,41,33,17,4407, -1, -1,-1],
[1370,2118,2938,931,34,24,22,-1, -1, -1,-1]]

distanceMap = [[3.66,3.02,3.37,2.02,2.47,1.96,3.82,2.18,3.99,2.47,1.55],
[3.92,3.26,3.21,1.87,1.54,2.3,2.1,2.05,3.25,1.85,1.61],
[2.66,2.34,2.69,3.33,3.62,2.69,2.88,3.96,2.55,3.43,3.05],
[3.41,2.77,2.81,2.89,1.79,1.57,2.75,1.9,3.64,3.34,3.78],
[2.19,3.9,1.68,3.91,2.34,1.64,2.51,3.52,2.86,1.93,3.62],
[2.14,3.53,2.11,2.82,2.05,3.44,3.94,2.04,2.14,3.32,3.87],
[2.34,2.41,1.65,3.83,1.69,3.42,3.52,3.85,3.89,3.91,2.26],
[2.73,2.86,2.03,2.75,2.05,1.62,2.02,2.49,1.76,2.87,2.82],
[2.15,1.89,2.09,1.94,3.26,3.23,2.86,2.52,2.56,3.76,2.05],
[3.71,2.73,3.54,2.97,1.54,2.24,2.44,3.61,2.36,3.77,3.61],
[1.56,3.38,2.45,2.35,2.87,2.02,3.4,3.87,2.49,3.53,3.85],
[2.75,3.98,3.94,1.97,3.4,2.71,2.8,2.07,2.86,3.35,3.46]]

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

realEstatePriceMap = [[-1,-1,71244,76723,-1,-1,-1, -1, -1,-1,-1],
[-1,-1,71823,69231,-1,-1,-1, -1, -1, -1,-1],
[71211,69102,86121,61136,67121,78942,109123, 110162, -1,-1,148065],
[70125,61348,66475,64721,72123,70958,64021, 100126, 72191,250123,279121],
[80121,52123,54872,461123,58123,70165,90786, -1, -1, 395647, 399729],
[178125,58195,70453,76412,100285,115834,385723,348576, 481272, -1,-1],
[90176,80653,75892,79304,97382,90327,92945,110245, 140283,-1,-1],
[60467,80128,90278,89288,86645,90172,102040,110284,90875,110243,-1],
[80127,90767,88938,78293,72845,69437,78293,90182,105623,-1,-1],
[79234,67328,90273,102940,110237,130283,138172,107824,107253,-1, -1],
[120123,13048,98274,123075,130856,135276,11212,142145, -1, -1,-1],
[100781,90465,120115,130552,120763,140589,140269,-1, -1, -1,-1]]

distanceCap = 12.94

def buildingCost(size, locationCostRatio):
  utilityCost = ( 9.17 + 2.61 + 3.59 + 1.81 + 0.93 + 1.43 + 3.85 + 2.76 ) * ( size ) 
  constructionCost = 25000 + ( 75 * size ) 
  return locationCostRatio * constructionCost + utilityCost

def storeCapacity(totalSize):
  dailyHours = 12
  tripsPerDay = 7 / 1.6 #7 days divided by 1.6 trips per week
  hoursPerTrip = 43 / 60
  capacityPerPerson = totalSize / 50 
  
  return capacityPerPerson * ( dailyHours / hoursPerTrip ) * tripsPerDay
  
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
  totalCount, distanceTravelled = 0, 0
  
  while queue: 
    x, y, distanceTravelled = queue.popleft()
    # totalCount += populationDensityMap[x][y] * has_access(medianHouseholdIncomeMap[i][j], distanceTravelled)
    coordinates = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    diagonals = [(x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)]
    currentSize = distanceMap[x][y]
    results.append([x, y, has_access(medianHouseholdIncomeMap[x][y], distanceTravelled)])
  	
    for i, j in coordinates:
      if not ([i,j] in visited or i < 0 or j < 0 or i >= n or j >= n or distanceTravelled > (distanceCap + straightDistance)):
        straightDistance = currentSize / 2 + distanceMap[i][j] / 2 
        queue.append((i, j, distanceTravelled + straightDistance))
        visited.add([i, j])
    
    for i, j in diagonals:
      if not ([i,j] in visited or i < 0 or j < 0 or i >= n or j >= n or distanceTravelled > (distanceCap + diagonalDistance)):
        diagonalDistance = (2 * ((currentSize / 2) ** 2)) ** 0.5 + (2 * ((distanceMap[i][j] / 2) ** 2)) ** 0.5
        queue.append((i, j, distanceTravelled + diagonalDistance))
        visited.add([i, j])
    locationAccessCache[[a,b]] = visited

def populateCache():
  for i in range(len(populationDensityMap)):
    for j in range(len(populactionDensityMap)):
      populationWithAccess(i, j)

# create descending list of location pairs in order of total population accessed, excluding duplicates between locations
def findLocationPairs():
	locationPairs = []
  seenPairs = set()
  for locationOne, accessedLocationsOne in locationAccessCache.items():
    for locationTwo, accessedLocationsTwo in locationAccesCache.items():
      if locationOne == locationTwo:
        continue
      if (locationOne, locationTwo) in seenPairs or (locationTwo, locationOne) in seenPairs:
        continue
  		accessScoreMap = collections.defaultdict(int)
      for accessedLocation in (accessedLocationsOne + accessedLocationsTwo):
      	accessScoreMap[(accessedLocation[0],accesssedLocation[1])] = max(accessedLocation[2], accessScoreMap[(accessedLocation[0],accesssedLocation[1])])
      totalAccessed = 0
      for location, accessScore in accessScoreMap.items():
        population = populationDensityMap[location[0]][location[1]] * (distanceMap[location[0]][location[1]] ** 2)* accessScore
        totalAccessed += population if population > 0 else 0
      locationPairs.append((locationOne, locationTwo), totalAccessed)
    	seenPairs.add((locationOne, locationTwo))
  locationPairs.sort(key = lambda x: x[1], reverse = True)
  return locationPairs

def findOptimalPair():
  locationPairs = findLocationPairs() 
  
def main():
  populateCache()

