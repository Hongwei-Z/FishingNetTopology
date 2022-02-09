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
        return [self.tip1, self.tip2]

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
        self.approve = 0

    def nextNode(self, data):  # Create new node in FNT
        self.tip_list.append([self.count, 0])  # Add new node to the tip list
        bound = triangularNums(self.rate)  # Triangular numbers, boundaries of the initial net
        count_tri = math.comb(self.rate + 1, 2)  # Counting nodes in the initial net
        height = self.rate * 2 - 1

        if self.count == 0:  # First node, #0, without tips
            node = Node(self.count, data, None, None)
            self.nodes.append(node)

        elif 0 < self.count < count_tri:

            if self.count in bound:  # Boundaries of the initial net with one tip
                node = Node(self.count, data, self.nextTip(), None)
                self.nodes.append(node)

            else:  # Other nodes of the initial net with two tips
                node = Node(self.count, data, self.nextTip(), self.nextTip())
                self.nodes.append(node)
        else:
            if self.atBoundary():
                if (self.count - count_tri + 1) % height == self.rate:
                    node = Node(self.count, data, self.nextTip(), self.nodes[self.count-self.rate+1].getIndex())
                    self.nodes.append(node)
                if (self.count - count_tri + 1) % height == 0:
                    node = Node(self.count, data, self.nextTip(), self.nodes[self.count-self.rate].getIndex())
                    self.nodes.append(node)

            else:
                node = Node(self.count, data, self.nodes[self.count-self.rate].getIndex(), self.nodes[self.count-self.rate+1].getIndex())
                self.nodes.append(node)

        self.count += 1

    def nextTip(self):
        bound = triangularNums(self.rate)  # Triangular numbers, boundaries of the initial net
        count_tri = math.comb(self.rate + 1, 2)  # Counting nodes in the initial net
        height = self.rate * 2 - 1

        if self.tip_list[0][1] >= 2:  # If node is approved twice, remove from the tip list
            self.tip_list.pop(0)

        tip = self.tip_list[0][0]
        self.tip_list[0][1] += 1

        if self.count > count_tri:
            if self.atBoundary():
                tip = (self.nodes[self.count - height].getIndex())
                self.tip_list[0][1] += 1

        return tip

    def atBoundary(self):
        count_tri = math.comb(self.rate + 1, 2)  # Counting nodes in the initial net
        height = self.rate * 2 - 1
        return (self.count - count_tri + 1) % height in [0, self.rate]

    def toString(self):
        for i in range(len(self.nodes)):
            self.nodes[i].toString()


def triangularNums(r):
    nums = []
    for n in range(1, r):
        upper = int(n * (n + 1) / 2)
        lower = upper + n
        nums.append(upper)
        nums.append(lower)
    return nums