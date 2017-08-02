import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
from functools import reduce


def iszero(a):
    return abs(a) < 1e-9


def gcd(a, b):
    if iszero(b):
        return a
    return gcd(b, a % b)


def gcdarr(arr):
    return reduce(gcd, arr)


def correctratios(arr):
    arrgcd = gcdarr(arr)
    list = [round(a / arrgcd) for a in arr]
    list.append(int(1 / arrgcd))
    return list[1:]


def getMatrix():
    #input = np.loadtxt("input.txt", dtype='i', delimiter=',')
    matrixList = []
    numFile = open("input.txt", "r")
    lines = numFile.readlines()
    for line in lines:
        line = line.split(',')
        row = []  # 1st change
        for i in line:
            row.append(int(i))  # 2nd change
        matrixList.append(row)  # 3rd change
    return matrixList

matrix = getMatrix()

noOfRows = int(len(matrix))
visited = [0] * noOfRows


# Create Directed Graph
G = nx.DiGraph()

# Add a list of nodes:
nodesList = []
for i in range(0, noOfRows):
    nodesList.append(i)
G.add_nodes_from(nodesList)

# # Add a list of edges:
edgeList = []
for i in range(0, noOfRows):
    for j in range(0, noOfRows):
        if matrix[i][j]:
            edgeList.append((i, j))
G.add_edges_from(edgeList)

print(G)

# Return a list of cycles described as a list o nodes
loop_list = list(nx.simple_cycles(G))
# print(loop_list)


sumList = []
for row in matrix:
    sum = 0
    for value in row:
        sum += value
    sumList.append(sum)

# print(sumList)

# end sum of row
# first level probablity
i = 0
for row in matrix:
    prob = []
    for value in row:
        if(sumList[i] is not 0):
            prob.append(value / sumList[i])
        else:
            prob.append(0)
    if(sumList[i] is not 0):
        matrix[i] = prob
    i += 1

# print(matrix)


vis =[False]* noOfRows
# end of first level probablity
def dfs(v,cost):
    vis[v] = True
    # print(matrix[v])
    for j,value in enumerate(matrix[v]):
        matrix[v][j]= cost*value
    print(matrix)
    for j,value in enumerate(matrix[v]):
        if j not in terminalList:
            if value and not vis[j]: 
                dfs(j,matrix[v][j])

    return

terminalList = []
i = 0
for values in matrix[i]:
    if all(p == 0 for p in matrix[i]):
        terminalList.append(i)
    i += 1
print(terminalList)
print(loop_list)
loop_costs = [1] * noOfRows
for loop in loop_list:
    loop_cost = 1
    for index, node in enumerate(loop):
        length = int(len(loop))
        loop_cost *=  matrix[loop[index]][loop[(index+1)%length]] 
    
    print(loop)
    for index,node in enumerate(loop):
        loop_costs[index] = loop_cost
        
print("loopcost")
print(loop_cost) 

dfs(0,1)

# second level probablity
# i=0
# for row in matrix:
#     for value in row:
#         if(sumList[i] is not 0):
#             prob.append(value / sumList[i])
#         else:
#             prob.append(0)
#     if(sumList[i] is not 0):
#         matrix[i] = prob
#     i+=1
# print(matrix)


# end of second level probablity
 
prob = [0] * noOfRows

# i = 0
# for i, value in matrix:
#     if value is not 0:
#         prob[i] = value / sumList[0]
#     i += 1
# i = 0
# for value in matrix[1]:
#     if value is not 0:
#         prob = value / sumList[1]
#         prob[i] = np.sum(prob)  # prob[i] * value/sumList[1]
#     i += 1

resultList = [0] * noOfRows 
i=0
for row in matrix:
    for j,value in enumerate(row):
        if j in terminalList:
            if value > 0.0:
                matrix[i][j] = np.sum((loop_costs[i]**ex)*value for ex in range(0,100) )
                resultList[j] = matrix[i][j]
    i+=1
print(resultList)
        # if value is not 0:
        #     prob = value / sumList[1]
        #     prob[i] = np.sum(prob)  # prob[i] * value/sumList[1]
        # i += 1

finalResultList = []

for i, value in enumerate(resultList):
    if i in terminalList:
        finalResultList.append(value)

print(prob)
prob = [0, 0, 3 / 14, 1 / 7, 9 / 14]
#prob = [0,0,.2142857,.142857,.642857]
#prob = [0,0,.2142857,.142857,.642857]

print(correctratios(finalResultList))
