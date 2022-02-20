# Fishing Net Topology
**A Novel Blockchain Structure for WSNs Based on IOTA Tangle**

### Structural Demonstration:
**Example with the rate of 10, including 1000 nodes.**
![FNT Structure Display](image/FNT_Structure.png)

### Files:
- **[FNT:](FNT.py) Main File of Fishing Net Topology, contains FNT class and Node class.**
- **[Visualization:](Visualization.py) Draw graphs related to FNT.**
- **[Test:](Test.ipynb) Experiments and feature showcases.**

### User Guide:
1. **Import libraries**
    ~~~
   import FNT
   import Visualization
    ~~~
2. **Create FNT, insert nodes**
    ~~~
   fnt = FNT.FishingNet(rate)
   fnt.nextNode(data, time)
    ~~~
3. **Functions**
    ~~~
   fnt.findNode(index)                 # Print a node
   fnt.findTips(index)                 # Print tips for this node
   fnt.findApprove(index)              # Find two nodes that approve this node
   fnt.findCW(index)                   # Compute the cumulative weight for a node
   fnt.disableNode(index)              # Detach a node
   fnt.printFNT()                      # Print all nodes
   
   Visualization.drawFNT(rate, nodes)  # Draw the FNT graph
   Visualization.drawCW(fnt)           # Draw the cw trend graph
    ~~~

### Terminology:
- **Initial Network:**
  - The part that allows the network to progressively reach maximum throughput.
  - The part used for network initialization, starting from node 0, each column has one more node than the previous one, until the number of nodes reaches the number of Rate. 
  - Form a triangle.
- **Formal Network:**
  - The formal network is the main part of the FNT. 
  - At this point, the network can reach maximum throughput.
  - The number of nodes in the first column is equal to Rate, and the second column is one smaller than Rate, these two columns form a Group.
  - The structure of the formal network is the repetition of the Group.
- **Rate:**
  - The data packet throughput in the network. 
  - The maximum number of packets going through the network at the same time.



### Structural Explanation:
**Example with the rate of 6, including 100 nodes.**
![FNT Structure Explain](image/Explain.png)

### Author
**Hongwei Zhang**