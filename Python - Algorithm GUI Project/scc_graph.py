# Algorthms GUI Project / scc_graph.py
# Created on: 07-Nov-2018
# Author: Gourav Siddhad

# Kosaraju's algorithm / Strongly Connected Components

from collections import defaultdict


class SCC_Graph:
    def __init__(self, vertices=0):
        self.V = vertices
        self.graph = defaultdict(list)

    def read_File(self, inputfile):
        vertices = 0
        with open(inputfile, 'r') as graphInput:
            for line in graphInput:
                vertices = vertices + 1

        self.V = vertices
        i = 0
        with open(inputfile, 'r') as graphInput:
            for line in graphInput:
                ints = [int(x) for x in line.split()]
                j = 0
                for v in ints:
                    if v:
                        self.addEdge(i, j)
                    j = j + 1
                i = i + 1

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        output = str(v) + ' '
        for i in self.graph[v]:
            if visited[i] == False:
                ch = self.DFSUtil(i, visited)
                output = output + ch
        return output

    def fillOrder(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    def getTranspose(self):
        g = SCC_Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def printSCCs(self):
        output = ''
        stack = []
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        gr = self.getTranspose()
        visited = [False] * (self.V)

        while stack:
            i = stack.pop()
            if visited[i] == False:
                ch = gr.DFSUtil(i, visited)
                output = output + ch + '\n'
        return output
