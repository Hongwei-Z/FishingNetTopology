# This file only used to draw the graph of FNT
import math
import networkx as nx
import matplotlib.pyplot as plt

import FNT


def draw_FNT(rate, total_nodes):
    fnt = nx.DiGraph()

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
    j = 0
    while j < nodes2:

        y1 = rate - 2
        y2 = rate - 1

        if index % 2 == 0:
            for m in range(rate - 1):
                position.append((x, y1))
                y1 -= 2
                j += 1
        else:
            for n in range(rate):
                position.append((x, y2))
                y2 -= 2
                j += 1

        x += 1
        index += 1

    # Create nodes
    for k in range(total_nodes):
        fnt.add_node(k, pos=position[k])

    # Add edges for all nodes in the triangle
    m = 0
    n = 0
    diff = []
    for p in range(rate):
        for g in range(p):
            diff.append((m, m + 1))
            n += 1
        m += 1
    for q in range(nodes1 - rate):
        fnt.add_edge(q + diff[q][0], q)
        fnt.add_edge(q + diff[q][1], q)

    # Add edges to rest of nodes
    columns = rate * 2 - 1
    diff2 = [(m, m - 1), (m - 1, m)]
    r = nodes1
    s = 0
    while r < total_nodes:

        if s < rate - 1:
            for j in range(rate - 1):
                if r < total_nodes:
                    fnt.add_edge(r, r - diff2[0][0])
                    fnt.add_edge(r, r - diff2[0][1])
                    r += 1
                    s += 1

        elif (rate - 1) <= s < columns:
            fnt.add_edge(r, r - columns)
            fnt.add_edge(r, r - diff2[1][0])
            r += 1
            s += 1
            for j in range(rate - 2):
                if r < total_nodes:
                    fnt.add_edge(r, r - diff2[0][0])
                    fnt.add_edge(r, r - diff2[0][1])
                    r += 1
                    s += 1
            if r < total_nodes:
                fnt.add_edge(r, r - diff2[1][1])
                fnt.add_edge(r, r - columns)
                r += 1
                s += 1

        else:
            s = 0

    plt.figure(1, figsize=(30, 20))
    nx.draw(fnt, position, with_labels=True)
    plt.show()
    print("Fishing Net Topology")
    print("Rate of {0}, {1} nodes.".format(rate, total_nodes))
