# Sensor: Sensor ID, Status, Location.
class Sensor(object):
    def __init__(self, sid, status, location):
        self.sid = sid
        self.status = status
        self.location = location


# Dataset: Data Type, Data.
class Dataset(object):
    def __init__(self, datatype, data):
        self.datatype = datatype
        self.data = data


class Packet(Sensor, Dataset):

    def __init__(self, pid, timestamp, auditee1, auditee2, sid, status, location, datatype, data):

        Sensor.__init__(self, sid, status, location)
        Dataset.__init__(self, datatype, data)

        self.pid = pid
        self.timestamp = timestamp
        self.auditee1 = auditee1
        self.auditee2 = auditee2
        self.auditor = []
        self.disable = False

    def print_packet(self):
        print("Packet: ")
        print("PID: {0}, Time: {1}, Auditee: {2}, {3}".format(self.pid, self.timestamp, self.auditee1, self.auditee2))
        print("SID: {0}, Status: {1}, Location: {2}".format(self.sid, self.status, self.location))
        print("Data Type: {0}, Data: {1}".format(self.datatype, self.data))



