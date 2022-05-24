# Node: Node ID, Timestamp.
class Node(object):
    def __init__(self, nid, timestamp):
        self.nid = nid
        self.timestamp = timestamp


# Sensor: Sensor ID, Status, Location.
class Sensor(object):
    def __init__(self, sid, status, location):
        self.sid = sid
        self.status = status
        self.location = location


# Database: Data Type, Data.
class Database(object):
    def __init__(self, datatype, data):
        self.datatype = datatype
        self.data = data


class Packet(Node, Sensor, Database):

    def __init__(self, nid, timestamp, sid, status, location, datatype, data):

        Node.__init__(self, nid, timestamp)
        Sensor.__init__(self, sid, status, location)
        Database.__init__(self, datatype, data)

        print("NID: {0}, Time: {1}".format(nid, timestamp))
        print("SID: {0}, Status: {1}, Location: {2}".format(sid, status, location))
        print("Data Type: {0}, Data: {1}".format(datatype, data))
