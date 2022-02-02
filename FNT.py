class Node(object):
    def __init__(self, index, data, source, timestamp):
        self.index = index
        self.data = data
        self.weight = 1
        self.source = source
        self.timestamp = timestamp

    def getIndex(self):
        return self.index

    def getData(self):
        return self.data

    def getWeight(self):
        return self.weight

    def weightUpdate(self):
        self.weight += 1

    def getSource(self):
        return self.source

    def getTimestamp(self):
        return self.timestamp

    def toString(self):
        print("Node {0}: Data: {1}, Weight: {2}, Source: {3}, Timestamp: {4}"
              .format(self.index, self.data, self.weight, self.source, self.timestamp))


#class FishingNet(object):