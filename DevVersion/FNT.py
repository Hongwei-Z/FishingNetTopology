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

    def get_index(self):
        return self.index

    def get_data(self):
        return self.data

    def get_time(self):
        return self.time

    def get_tips(self):  # Return index of two tips

        if self.tip1 is None and self.tip2 is None:
            return [None, None]

        elif self.tip1 is not None and self.tip2 is None:
            return [self.tip1.get_index(), None]

        elif self.tip2 is not None and self.tip1 is None:
            return [None, self.tip2.get_index()]

        else:
            return [self.tip1.get_index(), self.tip2.get_index()]

    def print_node(self):
        print("Node {0}, {1}, {2}, Tips: {3}"
              .format(self.get_index(), self.get_data(), self.get_time(), self.get_tips()))


class FishingNet(object):

    # An FNT contains rate and nodes
    def __init__(self, rate):
        self.count = 0
        self.rate = rate
        self.nodes = []
        self.tip_list = []

        self.bound = edge_nodes(self.rate)  # Triangular numbers, boundary of the initial network
        self.count_initial = math.comb(self.rate + 1, 2)  # Counting nodes in the initial network
        self.group = self.rate * 2 - 1  # Each group of nodes, contains (rate * 2 - 1) nodes

    def next_node(self, data, time):  # Create new node in FNT

        if self.count == 0:  # First node, #0, without tips
            node = Node(self.count, data, time, None, None)

        elif 0 < self.count < self.count_initial:  # Nodes in the initial network

            if self.count in self.bound:  # Boundaries of the initial network with one tip
                t = self.tips_initial()
                node = Node(self.count, data, time, t, None)
                t.approver.append(node)

            else:  # Other nodes of the initial network with two tips
                t1 = self.tips_initial()
                t2 = self.tips_initial()
                node = Node(self.count, data, time, t1, t2)
                t1.approver.append(node)
                t2.approver.append(node)

        else:  # Nodes in the formal network
            t1 = self.tips_formal()[0]
            t2 = self.tips_formal()[1]
            node = Node(self.count, data, time, t1, t2)
            t1.approver.append(node)
            t2.approver.append(node)

        self.tip_list.append([node, 0])
        self.nodes.append(node)
        self.count += 1

    def tips_initial(self):  # Tips for the initial network
        tip = self.tip_list[0][0]
        self.tip_list[0][1] += 1

        if self.tip_list[0][1] >= 2:  # If node is approved twice, remove from the tip list
            self.tip_list.pop(0)

        if self.count_initial < self.count and self.edge():  # Last column of the initial network
            tip = (self.nodes[self.count - self.group])
            self.tip_list[0][1] += 1

        return tip

    def tips_formal(self):  # Tips for the formal network

        if self.edge():  # Tips for boundary nodes

            if self.upper():  # Tips for upper bound nodes
                return [self.tips_initial(), self.nodes[self.count - self.rate + 1]]
            else:  # Tips for lower bound nodes
                return [self.tips_initial(), self.nodes[self.count - self.rate]]

        else:  # Tips for other nodes
            return [self.nodes[self.count - self.rate], self.nodes[self.count - self.rate + 1]]

    def find_node(self, index):  # Find and return the node
        if index >= self.count:
            return

        return self.nodes[index].print_node()

    def get_app_index(self, index):  # Return the index of two nodes that approve this node

        if index >= self.count or len(self.nodes[index].approver) == 0:
            return [None, None]

        elif len(self.nodes[index].approver) == 1:
            ap1 = self.nodes[index].approver[0].get_index()
            return [ap1, None]

        else:
            ap1 = self.nodes[index].approver[0].get_index()
            ap2 = self.nodes[index].approver[1].get_index()
            return [ap1, ap2]

    def find_approver(self, index):  # Print two nodes that approved this node
        apps = self.get_app_index(index)
        if apps[0] is not None and apps[1] is not None:
            self.find_node(apps[0])
            self.find_node(apps[1])

    def find_tips(self, index):  # Return two tips
        if index >= self.count:
            return

        # Index of two tips
        t1 = self.nodes[index].get_tips()[0]
        t2 = self.nodes[index].get_tips()[1]
        self.find_node(t1)
        self.find_node(t2)

    def disable_node(self, index):  # Detach a node
        if index >= self.count:
            return

        # Find related nodes and detach
        apps = self.get_app_index(index)
        t1 = self.nodes[apps[0]].get_tips()
        t2 = self.nodes[apps[1]].get_tips()

        if t1[0] == index:
            self.nodes[apps[0]].tip1 = None
        if t1[1] == index:
            self.nodes[apps[0]].tip2 = None
        if t2[0] == index:
            self.nodes[apps[1]].tip1 = None
        if t2[1] == index:
            self.nodes[apps[1]].tip2 = None

        self.nodes[index].disable = True  # Disable the node

    def print_fnt(self):  # Print all nodes
        for i in range(len(self.nodes)):
            if self.nodes[i].disable is True:
                print("Node {0} disabled".format(i))
            else:
                self.nodes[i].print_node()

    def edge(self):  # Determine whether a node is on the boundary
        return (self.count - self.count_initial + 1) % self.group in [0, self.rate]

    def upper(self):  # Determine whether a node is on the upper or lower boundary

        if (self.count - self.count_initial + 1) % self.group == self.rate:
            return True
        if (self.count - self.count_initial + 1) % self.group == 0:
            return False


def edge_nodes(r):  # Generate a list of with triangular numbers
    edge_nums = []
    for n in range(1, r):
        x = int(n * (n + 1) / 2)
        y = x + n
        edge_nums.append(x)
        edge_nums.append(y)
    return edge_nums
