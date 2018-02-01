"""
Name of Author : Amit Jagannath Magar
Version 1.0
Assignment No 1
email ajm6745@g.rit.edu
"""


import sys


# SearchGraph.py
#
# Implementation of iterative deepening search for use in finding optimal routes
# between locations in a graph. In the graph to be searched, nodes have names
# (e.g. city names for a map).
#
# An undirected graph is passed in as a text file (first command line argument).
#
# Usage: python SearchGraph.py graphFile startLocation endLocation
#
# Author: Richard Zanibbi, RIT, Nov. 2011
def read_graph(filename):
    """Read in edges of a graph represented one per line,
        using the format: srcStateName destStateName"""
    #print("Loading graph: " + filename)
    edges = {}

    inFile = open(filename)
    for line in inFile:
        roadInfo = line.split()

        # Skip blank lines, read in contents from non-empty lines.
        if (len(roadInfo) > 0):
            srcCity = roadInfo[0]
            destCity = roadInfo[1]

            if srcCity in edges:
                edges[srcCity] = edges[srcCity] + [destCity]
            else:
                edges[srcCity] = [destCity]

            if destCity in edges:
                edges[destCity] = edges[destCity] + [srcCity]
            else:
                edges[destCity] = [srcCity]

    #print("  done.\n")
    return edges


######################################
# Add functions for search, output
# etc. here
######################################

"""
This is Frontier class to represent Frontier Data structure
    it has 2 attributes
    stack :- A Queue with FIFO property
    lookup :- A set 
"""
class Frontier:
    __slot__ = "stack", "lookup"

    """
    Contructor of Class
    """
    def __init__(self):
        self.stack = []
        self.lookup = set()

    """
    This function returns top element of stack
    """
    def top(self):
        return self.stack[len(self.stack) - 1]
    """
    This function checks if stack is empty or not
        return True if stack is empty
                False if stack is not empty
    """

    def isEmpty(self):
        return self.stack == []

    """
    This function push element at top of stack and also in look up table
    """
    def push(self, node):
        self.stack.append(node)
        self.lookup.add(node.name)

    """
    This function removes first element from stack and return it also removes
    element from look up set
    """
    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            self.lookup.remove(self.top().name)
            return self.stack.pop()
    """
    This functions checks in lookup table if passed element is present in lookup table or not
    """
    def present(self, name):
        return self.lookup.__contains__(name)


"""
This class represents search node for iterative deepenig
    it has 3 attributes
    parent which represent parent link to parent
    name Name of City
    level represents cost to reach at search node
"""
class node:
    __slot__ = "parent", "name", "level"

    def __init__(self, name, parent, level):
        self.name = name
        self.parent = parent
        self.level = level


"""
This function performs Iterative Deepening DFS on graph until goal state is found or 
graph is exhausted
"""

def iterative_DFS(edges, start, end):
    limit = 0
    flag = 1
    visited={}
    while (flag):
        ##print ('limit =' + str(limit))
        test, max,list,solution,visited = depth_limited_dfs(edges, start, end, limit,visited)
        print('--------------- States Visited at Depth '+str(limit)+' ---------------')
        for item in list:
            print (2*item.level*' ',item.name)

        if test is 'Success':
            print('--  Solution for: ' + start + ' to ' + end + '-------------------')
            op=solution[::-1]
            print (op)
            return op
            break

        if(test == 'Fail' and max < limit):
            solution.append('Failed Search')
            return solution
            break
        limit = limit + 1

"""
This function performs Depth Limited DFS on given Graph upto given limit 
"""
def depth_limited_dfs(edges, start, end, limit,visited):
    front = Frontier()
    front.push(node(start, None, 0))
    max_level = 0
    level_list = []
    solution=[]
    while front.isEmpty() == False:
        temp = front.pop()

        if (temp.level > limit):
            continue

        if (temp.level > max_level):
            max_level = temp.level

        visited[temp.name] = temp;
        level_list.append(temp)
        if temp.name == end:
            parent = temp.name
            while parent is not None:
                solution.append(parent)
                parent = visited[parent].parent
            return 'Success', max_level,level_list,solution,visited
        else:
            for iter in edges[temp.name]:
                if iter not in visited and not front.present(iter):
                    front.push(node(iter, temp.name, temp.level + 1))
                elif iter in visited and visited[iter].level==(temp.level+1):
                    front.push(node(iter, temp.name, temp.level + 1))
                else:
                    continue

    return 'Fail', max_level,level_list,solution,visited


# TBD

#########################
# Main program
#########################
def main():
    if len(sys.argv) != 4:
        print('Usage: python SearchGraph.py graphFilename startNode goalNode')
        return
    else:
        # Create a dictionary (i.e. associative array, implemented as a hash
        # table) for edges in the map file, and define start and end states for
        # the search. Each dictionary entry key is a string for a location,
        # associated with a list of strings for the adjacent states (cities) in
        # the state space.
        edges = {}
        edges = read_graph(sys.argv[1])
        start = sys.argv[2]
        goal = sys.argv[3]

        # Comment out the following lines to hide the graph description.
        #print("-- Adjacent Cities (Transition/Successor Fn) ------------------------")
         #for location in edges.keys():
         #   s = '  ' + location + ':\n     '
         #   s = s + str(edges[location])
         #   print(s)

        if not start in edges.keys():
            print("Start location is not in the graph.")
        else:
            s=iterative_DFS(edges, start, goal)
            print ('Function Returned List containing ',s)
            #print('')
            #print('--------------- States Visited ----------------')
            #print('TBD - print search tree if solution is found, and each time max depth is reached.')
            #print('')
            #print('--  Solution for: ' + start + ' to ' + goal + '-------------------')
            #print('TBD - provide solution path or indicate failure.')
            #print('')


# Execute the main program.
main()

