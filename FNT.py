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

    def new_node(self, data):  # Create new node in FNT
        self.tip_list.append(self.count)  # Add new node to the tip list

        # If node is approved twice, remove from the tip list
        if self.approve == 2:
            self.tip_list.pop(0)
            self.approve = 0

        bound = triangular_nums(self.rate)  # triangular numbers
        count_tri = math.comb(self.rate + 1, 2)  # count nodes in the triangle
        height = self.rate * 2 - 1

        if self.count == 0:  # First node, #0, without tips
            node = Node(self.count, data, None, None)
            self.nodes.append(node)
            self.count += 1

        else:  # Nodes after #0
            if self.count < count_tri:
                # Nodes in triangular numbers with have one tip
                if self.count in bound:
                    node = Node(self.count, data, self.tip_list[0], None)
                    self.nodes.append(node)
                    self.approve += 1
                    self.count += 1

                # Regular nodes with two tips
                else:
                    t = self.tip_list[0]
                    self.tip_list.pop(0)
                    node = Node(self.count, data, t, self.tip_list[0])
                    self.nodes.append(node)
                    self.approve = 1
                    self.count += 1
            else:
                # need to do: find tips for nodes on the boundary
                if (self.count - count_tri + 1) % height in [0, 10]:
                    print(self.count)
                    self.count += 1
                else:
                    t = self.tip_list[0]
                    self.tip_list.pop(0)
                    node = Node(self.count, data, t, self.tip_list[0])
                    self.nodes.append(node)
                    self.approve = 1
                    self.count += 1

    def toString(self):
        for i in range(len(self.nodes)):
            self.nodes[i].toString()


def triangular_nums(r):
    nums = []
    for n in range(1, r):
        upper = int(n * (n + 1) / 2)
        lower = upper + n
        nums.append(upper)
        nums.append(lower)
    return nums
