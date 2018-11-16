# Algorthms GUI Project / tsort.py
# Created on: 07-Nov-2018
# Author: Gourav Siddhad
# Topological Sort

from tsort_graph import T_Graph, T_Vertex

class TSort:
    def __init__(self):
        self.graph = T_Graph()

    def read_File(self, inputFile):
        with open(inputFile, 'r') as graphInput:
            for line in graphInput:
                ints = [int(x) for x in line.split()]
                src = ints[0]
                for i in range(1, len(ints)):
                    self.graph.add_edge(src, ints[i])

    def display_vertices(self):
        print(' Vertices: ', end='')
        for v in self.graph:
            print(v.get_key(), end=' ')

    def display_edges(self):
        print(' ')
        print('Edges: ')
        for v in self.graph:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(
                    v.get_key(), dest.get_key(), w))
            print()

    def display_graph(self):
        output = ''
        for v in self.graph:
            output = output + str(v.get_key()) + ' | '
            for dest in v.get_neighbours():
                output = output + str(dest.get_key()) + ' '
            output = output + '\n'
        return output

    def display_sorting(self):
        tlist = self.get_topological_sorting()
        output = '\n'
        if tlist is not None:
            output = output + 'Topological Sorting\n'
            output = output + str(tlist)
        else:
            output = output + 'Graph is not a DAG.'
        return output

    def get_topological_sorting_helper(self, v, visited, on_stack, tlist):
        if v in on_stack:
            return False

        on_stack.add(v)
        for dest in v.get_neighbours():
            if dest not in visited:
                if not self.get_topological_sorting_helper(dest, visited, on_stack, tlist):
                    return False
        on_stack.remove(v)
        visited.add(v)
        tlist.insert(0, v.get_key())  # prepend node key to tlist
        return True

    def get_topological_sorting(self):
        tlist = []
        visited = set()
        on_stack = set()
        for v in self.graph:
            if v not in visited:
                if not self.get_topological_sorting_helper(v, visited, on_stack, tlist):
                    return None
        return tlist
