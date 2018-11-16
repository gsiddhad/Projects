# Algorthms GUI Project / mst_graph.py
# Created on: 07-Nov-2018
# Author: Gourav Siddhad
# Minimum Spanning Tree

from math import sqrt
import sys


class MST_Graph():
    def __init__(self, vertices=0):
        self.V = vertices

    def read_File(self, inputFile):
        vertices = 0
        with open(inputFile, 'r') as graphInput:
            for line in graphInput:
                vertices = vertices + 1

        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.cord = [[0 for column in range(2)]
                     for row in range(vertices)]
        self.V = vertices

        i = 0
        with open(inputFile, 'r') as graphInput:
            for line in graphInput:
                ints = [int(x) for x in line.split()]
                self.cord[i][0] = ints[0]
                self.cord[i][1] = ints[1]
                i = i + 1
        self.calculate_edges()

    def calculate_edges(self):
        for a in range(self.V):
            for b in range(self.V):
                self.graph[a][b] = sqrt(
                    (self.cord[a][1] - self.cord[b][1])**2 + (self.cord[a][0] - self.cord[b][0])**2)

    def display_cord(self):
        for a in range(self.V):
            print(self.cord[a])

    def display_edges(self):
        for a in range(self.V):
            for b in range(self.V):
                print(self.cord[a], ',', self.cord[b], end=' ')
                print(' - ', self.graph[a][b])

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

    def double_prim(self, parent):
        for i in range(1, self.V):
            self.graph[i][parent[i]] = sys.maxsize
            self.graph[parent[i]][i] = sys.maxsize

    def printMST(self, parent):
        output = ''
        output = output + 'Edge \t\tWeight'
        for i in range(1, self.V):
            output = output + '\n' + str(self.cord[parent[i]])
            output = output + '-' + str(self.cord[i])
            output = output + '\t' + str(self.graph[i][int(parent[i])])
        return output
