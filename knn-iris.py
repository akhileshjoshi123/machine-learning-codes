import random
import csv

split = 0.66

with open('C:/Users/Thinkpad T540P/Desktop/meri mehnat/knn iris/iris-data.txt') as csvfile:
    lines = csv.reader(csvfile)
    dataset = list(lines)

random.shuffle(dataset)

div = int(split * len(dataset))
train = dataset [:div]
test = dataset [div:]


import math
# square root of the sum of the squared differences between the two arrays of numbers
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)



import operator
distances = []
def getNeighbors(trainingSet, testInstance, k):
	#distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

import operator  
classVotes = {}
def getResponse(neighbors):
	#classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

predictions=[]

k = 3


for x in range(len(test)):
    neighbors = getNeighbors(train, test[x], k)
    result = getResponse(neighbors)
    predictions.append(result)
    print('> predicted=' + repr(result) + ', actual=' + repr(test[x][-1]))
    accuracy = getAccuracy(test, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')


