import math


class Node(object):

    # A node may contain index, data, two tips, and other info
    def __init__(self, index, data, tip1, tip2):
        self.index = index
        self.data = data
        self.tip1 = tip1
        self.tip2 = tip2
        # self.source = source
        # self.time = time

    def getIndex(self):
        return self.index

    def getData(self):
        return self.data

    def getTips(self):
        if self.tip1 is None and self.tip2 is None:
            return [None, None]
        elif self.tip1 is not None and self.tip2 is None:
            return [self.tip1.getIndex(), None]
        elif self.tip2 is not None and self.tip1 is None:
            return [None, self.tip2.getIndex()]
        else:
            return [self.tip1.getIndex(), self.tip2.getIndex()]

    # def getSource(self):
    #     return self.source
    #
    # def getTime(self):
    #     return self.time

    def toString(self):
        print("Node {0}, Data: {1}, Tips: {2}"
              .format(self.getIndex(), self.getData(), self.getTips()))


class FishingNet(object):

    # An FNT contains rate and nodes
    def __init__(self, rate):
        self.count = 0
        self.rate = rate
        self.nodes = []
        self.tip_list = []

        self.bound = triangularNums(self.rate)  # Triangular numbers, boundary of the initial network
        self.count_tri = math.comb(self.rate + 1, 2)  # Counting nodes in the initial network
        self.group = self.rate * 2 - 1  # Each group of nodes, contains (rate * 2 - 1) nodes

    def nextNode(self, data):  # Create new node in FNT

        if self.count == 0:  # First node, #0, without tips
            node = Node(self.count, data, None, None)

        elif 0 < self.count < self.count_tri:  # Nodes in the initial network

            if self.count in self.bound:  # Boundaries of the initial network with one tip
                node = Node(self.count, data, self.nextTip(), None)
            else:  # Other nodes of the initial network with two tips
                node = Node(self.count, data, self.nextTip(), self.nextTip())

        else:  # Nodes in the formal network
            node = Node(self.count, data, self.nextTipGroup()[0], self.nextTipGroup()[1])

        self.tip_list.append([node, 0])
        self.nodes.append(node)
        self.count += 1

    def nextTip(self):  # Tips for the initial network

        tip = self.tip_list[0][0]
        self.tip_list[0][1] += 1

        if self.tip_list[0][1] >= 2:  # If node is approved twice, remove from the tip list
            self.tip_list.pop(0)

        if self.count_tri < self.count and self.atBoundary():  # Last column of the initial network
            tip = (self.nodes[self.count - self.group])
            self.tip_list[0][1] += 1

        return tip

    def nextTipGroup(self):  # Tips for the formal network
        if self.atBoundary():  # Tips for boundary nodes

            if self.upper():  # Tips for upper bound nodes
                return [self.nextTip(), self.nodes[self.count - self.rate + 1]]
            else:  # Tips for lower bound nodes
                return [self.nextTip(), self.nodes[self.count - self.rate]]

        else:  # Tips for other nodes
            return [self.nodes[self.count - self.rate], self.nodes[self.count - self.rate + 1]]

    def atBoundary(self):  # Determine whether a node is on the boundary
        return (self.count - self.count_tri + 1) % self.group in [0, self.rate]

    def upper(self):  # Determine whether a node is on the upper or lower boundary
        if (self.count - self.count_tri + 1) % self.group == self.rate:
            return True
        if (self.count - self.count_tri + 1) % self.group == 0:
            return False

    def toString(self):
        for i in range(len(self.nodes)):
            self.nodes[i].toString()


def triangularNums(r):  # Generate a list of with triangular numbers
    nums = []
    for n in range(1, r):
        upper = int(n * (n + 1) / 2)
        lower = upper + n
        nums.append(upper)
        nums.append(lower)
    return nums
