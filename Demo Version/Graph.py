import math
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import FNT


def drawFNT(f):  # Draw the FNT graph
    fnt = nx.DiGraph()

    # Compute the number of nodes in triangle, and the rest nodes
    nodes1 = math.comb(f.rate + 1, 2)
    nodes2 = f.count - nodes1

    position = []  # Position of nodes

    # Find the positions of all nodes in the triangle
    for x in range(f.rate):
        y = x

        for i in range(x + 1):
            position.append((x, y))
            y -= 2

    # Find the positions of rest nodes
    index = 0
    x = f.rate
    j = 0

    while j < nodes2:

        y1 = f.rate - 2
        y2 = f.rate - 1

        if index % 2 == 0:

            for m in range(f.rate - 1):
                position.append((x, y1))
                y1 -= 2
                j += 1

        else:

            for n in range(f.rate):
                position.append((x, y2))
                y2 -= 2
                j += 1

        x += 1
        index += 1

    # Create nodes
    for k in range(f.count):
        fnt.add_node(k, pos=position[k])

    # Add edges for all nodes in the triangle
    m = 0
    n = 0
    diff = []

    for p in range(f.rate):

        for g in range(p):
            diff.append((m, m + 1))
            n += 1

        m += 1

    for q in range(nodes1 - f.rate):
        fnt.add_edge(q + diff[q][0], q)
        fnt.add_edge(q + diff[q][1], q)

    # Add edges to rest of nodes
    columns = f.rate * 2 - 1
    diff2 = [(m, m - 1), (m - 1, m)]
    r = nodes1
    s = 0

    while r < f.count:

        if s < f.rate - 1:

            for j in range(f.rate - 1):

                if r < f.count:
                    fnt.add_edge(r, r - diff2[0][0])
                    fnt.add_edge(r, r - diff2[0][1])
                    r += 1
                    s += 1

        elif (f.rate - 1) <= s < columns:

            fnt.add_edge(r, r - columns)
            fnt.add_edge(r, r - diff2[1][0])
            r += 1
            s += 1

            for j in range(f.rate - 2):

                if r < f.count:
                    fnt.add_edge(r, r - diff2[0][0])
                    fnt.add_edge(r, r - diff2[0][1])
                    r += 1
                    s += 1

            if r < f.count:
                fnt.add_edge(r, r - diff2[1][1])
                fnt.add_edge(r, r - columns)
                r += 1
                s += 1

        else:
            s = 0

    plt.figure(1, figsize=(30, 15))
    nx.draw(fnt, position, with_labels=True)
    plt.show()

    print("Fishing Net Topology")
    print("Rate of {0}, {1} nodes.".format(f.rate, f.count))


def drawCWs(f):  # Draw a graph to display the CWs of all nodes
    cw = []
    n = []

    for t in range(f.count):  # Compute cw for each node
        cw.append(f.findCW(t))
        n.append(t)

    # Draw the line chart for cw
    plt.figure(2, figsize=(15, 10))
    plt.title("Cumulative weight of all nodes")
    plt.xlabel("Node Index")
    plt.ylabel("Cumulative Weight")
    plt.plot(n, cw, linewidth=3, color='b', marker='o', markerfacecolor='r')
    plt.show()


def drawCWChg(f, index):
    # Draw a graph of the change of the CW of a node as the number of nodes increases

    cws = []
    interval = []
    f2 = FNT.FishingNet(f.rate)

    for b in range(f.count):
        f2.nextNode(None, None)
        if b % 10 == 0:
            cws.append(f2.findCW(index))
            interval.append(b)

    cws.append(f2.findCW(index))
    interval.append(f2.count)

    plt.figure(3, figsize=(15, 10))
    plt.title("The cumulative weight of node " + str(index) + " changes as the number of nodes increases")
    plt.xlabel("Total Nodes")
    plt.ylabel("Cumulative Weight of Node " + str(index))
    plt.plot(interval, cws)
    plt.show()


def drawThroughput(f):  # Draw the graph to show the throughput of each layer
    tp = f.findThroughput()
    layers = np.arange(1, len(tp) + 1)

    plt.figure(4, figsize=(15, 10))
    plt.title("The throughput of each layer")
    plt.xlabel("Layers")
    plt.ylabel("Throughput")
    plt.plot(layers, tp)
    plt.show()


def drawUtilization(f):  # Draw the graph to show the utilization of each layer
    ut = f.findUtilization()
    layers = np.arange(1, len(ut) + 1)

    plt.figure(5, figsize=(15, 10))
    plt.title("The utilization of each layer")
    plt.xlabel("Layers")
    plt.ylabel("Utilization")
    plt.ylim(0, 1.1)
    plt.plot(layers, ut)
    plt.show()


def drawWasteRate(f):  # Draw the graph to show the waste rate of each layer
    ws = f.findWaste()
    layers = np.arange(1, len(ws) + 1)

    plt.figure(6, figsize=(15, 10))
    plt.title("The waste rate of each layer")
    plt.xlabel("Layers")
    plt.ylabel("Waste Rate")
    plt.ylim(0, 1.1)
    plt.plot(layers, ws)
    plt.show()


def drawCumWaste(f):  # Draw the graph to show the cumulative waste rate
    cws = f.findCumWaste()
    layers = np.arange(1, len(cws) + 1)

    plt.figure(7, figsize=(15, 10))
    plt.title("The cumulative waste rate")
    plt.xlabel("Layers")
    plt.ylabel("Cumulative Waste Rate")
    plt.ylim(0, 1.1)
    plt.plot(layers, cws)
    plt.show()
