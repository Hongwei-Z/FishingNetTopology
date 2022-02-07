# This file only used to draw the graph of FNT
import math
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Define the rate of FNT, and total nodes
rate = 10
total_nodes = 100

# Compute the number of nodes in triangle, and the rest nodes
nodes1 = math.comb(rate + 1, 2)
nodes2 = total_nodes - nodes1

position = []  # Position of nodes

# Find the positions of all nodes in the triangle
for x in range(rate):
    y = x
    for i in range(x + 1):
        position.append((x, y))
        y -= 2

# Find the positions of rest nodes
index = 0
x = rate
i = 0
while i < nodes2:
    y1 = rate - 2
    y2 = rate - 1
    if index % 2 == 0:
        for m in range(rate - 1):
            position.append((x, y1))
            y1 -= 2
            i += 1
    else:
        for n in range(rate):
            position.append((x, y2))
            y2 -= 2
            i += 1
    x += 1
    index += 1

# Create nodes
for j in range(total_nodes):
    G.add_node(j, pos=position[j])

# Add edges for all nodes in the triangle
m = 0
n = 0
diff = []
for k in range(rate):
    for g in range(k):
        diff.append((m, m + 1))
        n += 1
    m += 1
for i in range(nodes1 - rate):
    G.add_edge(i + diff[i][0], i)
    G.add_edge(i + diff[i][1], i)

# Add edges to rest of nodes
lines = rate * 2 - 1
diff2 = [(m, m - 1), (m - 1, m)]
h = 0
r = nodes1
while r < total_nodes:
    if h < rate - 1:
        for j in range(rate - 1):
            if r < total_nodes:
                G.add_edge(r, r - diff2[0][0])
                G.add_edge(r, r - diff2[0][1])
                h += 1
                r += 1
    elif rate - 1 <= h < lines:
        G.add_edge(r, r - lines)
        G.add_edge(r, r - diff2[1][0])
        r += 1
        h += 1
        for j in range(rate - 2):
            if r < total_nodes:
                G.add_edge(r, r - diff2[0][0])
                G.add_edge(r, r - diff2[0][1])
                h += 1
                r += 1
        G.add_edge(r, r - diff2[1][1])
        G.add_edge(r, r - lines)
        h += 1
        r += 1
    else:
        h = 0

print("Number of nodes", len(G.nodes))
print("Number of edges", len(G.edges))
plt.figure(1, figsize=(30, 15))
nx.draw(G, position, with_labels=True)
plt.show()
