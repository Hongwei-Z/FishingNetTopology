class Node(object):

    # A node contains index, data, and two tips
    def __init__(self, index, data, tip1, tip2):
        self.index = index
        self.data = data
        self.tip1 = tip1
        self.tip2 = tip2

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

    def __init__(self, rate):
        self.count = 0
        self.rate = rate
        self.nodes = []
        self.tip_list = []
        self.approve = 0

    def new_node(self, data):
        self.tip_list.append(self.count)  # Add node to tip list

        # If tip is approved twice, remove from tip list
        if self.approve == 2:
            self.tip_list.pop(0)
            self.approve = 0

        boundary = self.boundary(self.rate)  # triangular numbers

        if self.count == 0:  # First node, #0, without tips
            node = Node(self.count, data, None, None)
            self.nodes.append(node)
            self.count += 1

        else:  # Nodes after #0

            # Nodes in triangular numbers, have one tip
            if self.count in boundary:
                node = Node(self.count, data, self.tip_list[0], None)
                self.nodes.append(node)
                self.approve += 1
                self.count += 1

            # Regular nodes, have two tips
            else:
                t = self.tip_list[0]
                self.tip_list.pop(0)
                node = Node(self.count, data, t, self.tip_list[0])
                self.nodes.append(node)
                self.approve = 1
                self.count += 1

    def boundary(self, r):
        bound = []
        for n in range(1, r):
            upper = int(n * (n + 1) / 2)
            lower = upper + n
            bound.append(upper)
            bound.append(lower)
        return bound

    def toString(self):
        for i in range(len(self.nodes)):
            self.nodes[i].toString()
