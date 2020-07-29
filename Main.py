import Edge
import FileProcess
import KruskalAlgorithm
import Graph
import SteinerTree

# Reading file

# FILENAME = input("Enter the file's name : ")

FILENAME = "Data/hc9u.stp"

inputFile = open(FILENAME, "r")

# _____________________________________________________________________________________________________________________________
# Process

tuple = FileProcess.fileProcess(inputFile.read())

inputFile.close()

Edges = tuple[4]
connectedNodes = tuple[3]
terminalNodes = tuple[5]
edgesNum = tuple[1]  # number of edges
nodesNum = tuple[0]  # number of nodes
terminalsNum = tuple[2]  # number of nodes



newEdges = KruskalAlgorithm.KruskalAlgorithm(Edges, connectedNodes, nodesNum, edgesNum)


newEdges = SteinerTree.buildSteinerTree(nodesNum, terminalNodes, connectedNodes, newEdges)




outputFile = open("Output/" + FILENAME.split("/")[1].split('.')[0] + '.out', 'w')
cost = Graph.calculateCost(newEdges)
ne = len(newEdges)

lines = [f"Cost {cost}\n", f"Edges {ne}\n"]
for i in newEdges:
    lines.append(f"E {i.firstNode} {i.secondNode}\n")

outputFile.writelines(lines)
