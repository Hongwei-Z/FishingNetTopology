import math


class Node(object):

    # A node may contain index, data, two tips, and other info
    def __init__(self, index, data, time, tip1, tip2):
        self.index = index
        self.data = data
        self.time = time
        self.tip1 = tip1
        self.tip2 = tip2

        self.approver = []
        self.disable = False

    def getIndex(self):
        return self.index

    def getData(self):
        return self.data

    def getTime(self):
        return self.time

    def getTips(self):  # Return index of two tips

        if self.tip1 is None and self.tip2 is None:
            return [None, None]

        elif self.tip1 is not None and self.tip2 is None:
            return [self.tip1.getIndex(), None]

        elif self.tip2 is not None and self.tip1 is None:
            return [None, self.tip2.getIndex()]

        else:
            return [self.tip1.getIndex(), self.tip2.getIndex()]

    def printNode(self):
        print("Node {0}, {1}, {2}, Tips: {3}"
              .format(self.getIndex(), self.getData(), self.getTime(), self.getTips()))


class FishingNet(object):

    # An FNT contains rate and nodes
    def __init__(self, rate):
        self.count = 0
        self.rate = rate
        self.nodes = []
        self.tipList = []
        self.cwRelated = []

        self.bound = triangularNums(self.rate)  # Triangular numbers, boundary of the initial network
        self.countTri = math.comb(self.rate + 1, 2)  # Counting nodes in the initial network
        self.group = self.rate * 2 - 1  # Each group of nodes, contains (rate * 2 - 1) nodes

    def nextNode(self, data, time):  # Create new node in FNT

        if self.count == 0:  # First node, #0, without tips
            node = Node(self.count, data, time, None, None)

        elif 0 < self.count < self.countTri:  # Nodes in the initial network

            if self.count in self.bound:  # Boundaries of the initial network with one tip

                t = self.nextTip()
                node = Node(self.count, data, time, t, None)
                t.approver.append(node)

            else:  # Other nodes of the initial network with two tips

                t1 = self.nextTip()
                t2 = self.nextTip()
                node = Node(self.count, data, time, t1, t2)
                t1.approver.append(node)
                t2.approver.append(node)

        else:  # Nodes in the formal network

            t1 = self.nextTipGroup()[0]
            t2 = self.nextTipGroup()[1]
            node = Node(self.count, data, time, t1, t2)
            t1.approver.append(node)
            t2.approver.append(node)

        self.tipList.append([node, 0])
        self.nodes.append(node)
        self.count += 1

    def nextTip(self):  # Tips for the initial network

        tip = self.tipList[0][0]
        self.tipList[0][1] += 1

        if self.tipList[0][1] >= 2:  # If node is approved twice, remove from the tip list
            self.tipList.pop(0)

        if self.countTri < self.count and self.atBoundary():  # Last column of the initial network
            tip = (self.nodes[self.count - self.group])
            self.tipList[0][1] += 1

        return tip

    def nextTipGroup(self):  # Tips for the formal network

        if self.atBoundary():  # Tips for boundary nodes

            if self.upper():  # Tips for upper bound nodes
                return [self.nextTip(), self.nodes[self.count - self.rate + 1]]

            else:  # Tips for lower bound nodes
                return [self.nextTip(), self.nodes[self.count - self.rate]]

        else:  # Tips for other nodes
            return [self.nodes[self.count - self.rate], self.nodes[self.count - self.rate + 1]]

    def findNode(self, index):  # Find and return the node

        if index is None:
            return

        if index >= self.count:
            return

        return self.nodes[index].printNode()

    def disableNode(self, index):  # Detach a node

        if index >= self.count:
            return

        # Find related nodes and detach
        x = int(self.getAp(index)[0])
        y = int(self.getAp(index)[1])
        t1 = self.nodes[x].getTips()
        t2 = self.nodes[y].getTips()

        if t1[0] == index:
            self.nodes[x].tip1 = None
        if t1[1] == index:
            self.nodes[x].tip2 = None
        if t2[0] == index:
            self.nodes[y].tip1 = None
        if t2[1] == index:
            self.nodes[y].tip2 = None

        self.nodes[index].disable = True  # Disable the node

    def findTips(self, index):  # Return two tips

        if index >= self.count:
            return

        # Index of two tips
        n1 = self.nodes[index].getTips()[0]
        n2 = self.nodes[index].getTips()[1]

        self.findNode(n1)
        self.findNode(n2)

    def getAp(self, index):  # Return the index of two nodes that approve this node

        if index not in self.cwRelated:
            self.cwRelated.append(index)

        if index >= self.count:
            return [None, None]

        if len(self.nodes[index].approver) == 0:
            return [None, None]

        elif len(self.nodes[index].approver) == 1:
            ap1 = self.nodes[index].approver[0].getIndex()
            return [ap1, None]

        else:
            ap1 = self.nodes[index].approver[0].getIndex()
            ap2 = self.nodes[index].approver[1].getIndex()
            return [ap1, ap2]

    def findApprover(self, index):  # Print two nodes that approved this node
        self.findNode(self.getAp(index)[0])
        self.findNode(self.getAp(index)[1])

    def cw(self, index):  # Counting all related nodes

        ap1 = self.getAp(index)[0]
        ap2 = self.getAp(index)[1]

        if ap1 is None and ap2 is None:
            return 0

        if ap1 is not None and ap2 is None:
            return 1 + self.cw(ap1)

        if ap1 is None and ap2 is not None:
            return 1 + self.cw(ap2)

        if ap1 is not None and ap2 is not None:
            return 2 + self.cw(ap1) + self.cw(ap2)

    def findCW(self, index, export=False):  # Return cumulative weight

        if index >= self.count:
            return 0

        if index == 0:
            return self.count

        self.cw(index)

        if export:  # Print all nodes followed this node
            self.cwRelated.sort()
            for j in self.cwRelated:
                self.findNode(j)
            return

        result = len(self.cwRelated)
        self.cwRelated.clear()

        return result

    def findSubnet(self, index):  # Return all nodes that directly or indirectly approved this node
        return self.findCW(index, True)

    def findThroughput(self):  # Return the list of throughput at each layer
        throughput = []

        for k in range(1, self.rate + 1):
            throughput.append(k)

        rest = self.count - math.comb(self.rate + 1, 2)

        while rest - self.rate + 1 >= 0 or rest - self.rate >= 0:

            if rest - self.rate + 1 >= 0:
                throughput.append(self.rate - 1)
                rest -= (self.rate - 1)

            if rest - self.rate >= 0:
                throughput.append(self.rate)
                rest -= self.rate

        if rest > 0:
            throughput.append(rest)

        return throughput

    def findUtilization(self):  # Calculate the utilization of each layer
        tp = self.findThroughput()
        ut = [round(m / self.rate, 4) for m in tp]

        return ut

    def findWaste(self):  # Calculate the waste rate of each layer
        ut = self.findUtilization()
        ws = [round(1 - s, 4) for s in ut]

        return ws

    def findCumWaste(self):  # Compute cumulative waste
        tp = self.findThroughput()
        cw = [self.rate - w for w in tp]

        cwa = []
        x = 0

        for z in cw:
            x += z
            cwa.append(x)

        for y in range(1, len(cwa) + 1):
            cwa[y - 1] /= self.rate * y

        cwa = [round(c, 4) for c in cwa]
        return cwa

    def findWasteRate(self):  # Calculate the waste rate of entire network
        Tn = math.comb(self.rate + 1, 2)
        F = math.pow(self.rate, 2) + (2 * self.rate * ((self.count - Tn) / (2 * self.rate - 1)))
        W = math.pow(self.rate, 2) - Tn + ((self.count - Tn) / (2 * self.rate - 1))
        WR = '{:.4%}'.format(W / F)

        return WR

    def printFNT(self):  # Print all nodes

        for i in range(len(self.nodes)):

            if self.nodes[i].disable is True:
                print("Node {0} disabled".format(i))

            else:
                self.nodes[i].printNode()

    def atBoundary(self):  # Determine whether a node is on the boundary
        return (self.count - self.countTri + 1) % self.group in [0, self.rate]

    def upper(self):  # Determine whether a node is on the upper or lower boundary

        if (self.count - self.countTri + 1) % self.group == self.rate:
            return True

        if (self.count - self.countTri + 1) % self.group == 0:
            return False


def triangularNums(r):  # Generate a list of with triangular numbers
    nums = []

    for n in range(1, r):
        upper = int(n * (n + 1) / 2)
        lower = upper + n
        nums.append(upper)
        nums.append(lower)

    return nums
