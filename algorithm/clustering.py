import math as math
import random as random
import numpy as numpy
from scipy.spatial import distance


def sorting(elem):
    return elem.y

class objects:
    def __init__(self, nome, data, cluster):
        self.nome = nome
        self.data = data
        self.closest = self
        self.cluster = cluster


class ot:
    def __init__(self, a, b, y):
        self.a = a
        self.b = b
        self.y = y


class kMeans:

    def __init__(self, nClusters, nIterations, data, path):
        self.nClusters = nClusters  # int com a quantidade
        self.nIterations = nIterations  # int com a quantidade
        self.data = data  # array com objects
        self.rows = len(data)  # int com a quantidade de linhas
        self.path = path
        # inicializa os centroides
        centroids = []
        for i in range(nClusters):
            centroids.append(data[random.randint(0, self.rows-1)])

        # array com posicoes dos centroids, tipo x e y, que são objects tambem
        self.centroids = centroids

        # inicializa dataCentroid com [] para ser uzada em findCentroidForDataPoint
        dataCentroid = []
        for i in range(self.rows):
            # array de int com o numero do centroid para cada posicao de dado
            dataCentroid.append([])
        self.dataCentroid = dataCentroid  # lista de int

        # inicializa cada dado para seu respectivo centroide
        auxit = self.rows
        for dataPos in range(auxit):
            self.findCentroidForDataPoint(dataPos)

        partitions = [[]for i in range(self.nClusters)]
        for j in range(auxit):
            partitions[self.dataCentroid[j]].append(self.data[j])
        self.partitions = partitions  # lista de listas de objects

    def findCentroidForDataPoint(self, dataPos):
        for i in range(self.nClusters):
            if(self.dataCentroid[dataPos] == []):
                self.dataCentroid[dataPos] = i

            distanceNow = float(distance.euclidean(
                self.centroids[self.dataCentroid[dataPos]].data, self.data[dataPos].data))

            newDistance = float(distance.euclidean(
                self.centroids[i].data, self.data[dataPos].data))

            if(distanceNow > newDistance):
                self.dataCentroid[dataPos] = i

    def fit(self):
        a = 0
        for i in range(self.nIterations):
            print(a)
            a += 1
            self.remakeCentroids()
            for dataPos in range(self.rows):
                self.findCentroidForDataPoint(dataPos)

            self.setPartitions()
        for j in range(self.rows):
            self.data[j].cluster = self.dataCentroid[j]

    def remakeCentroids(self):
        a = 0
        for p in self.partitions:
            x = 0
            y = 0
            l = 0
            for d in p:
                x += d.data[0]
                y += d.data[1]
                l += 1
            if l == 0:
                l = 1
            self.centroids[a].data[0] = x/l
            self.centroids[a].data[1] = y/l
            a = a+1

    def setPartitions(self):
        self.partitions = [[]
                           for i in range(self.nClusters)]  # reset partitions
        for j in range(self.rows):
            self.partitions[self.dataCentroid[j]].append(
                self.data[j])  # findin new partitions
