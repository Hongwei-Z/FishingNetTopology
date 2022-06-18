import math


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


# Packet: Packet ID, Timestamp, Auditee, Auditor, Sensor Info, Dataset.
class Packet(Sensor, Dataset):

    def __init__(self, pid, timestamp, sid, status, location, datatype, data, auditee1, auditee2):
        Sensor.__init__(self, sid, status, location)
        Dataset.__init__(self, datatype, data)
        self.pid = pid
        self.timestamp = timestamp
        self.auditee1 = auditee1
        self.auditee2 = auditee2
        self.auditor = []
        self.disable = False

    def get_pid(self):
        return self.pid

    def get_timestamp(self):
        return self.timestamp

    def get_auditee(self):
        a1 = self.auditee1
        a2 = self.auditee2
        if a1 is None and a2 is None:
            return [None, None]
        elif a1 is not None and a2 is None:
            return [a1.get_pid(), None]
        elif a2 is not None and a1 is None:
            return [None, a2.get_pid()]
        else:
            return [a1.get_pid(), a2.get_pid()]

    def get_sid(self):
        return self.sid

    def get_status(self):
        return self.status

    def get_location(self):
        return self.location

    def get_datatype(self):
        return self.datatype

    def get_data(self):
        return self.data

    def print_sensor(self):
        print("Sensor ID: {0}, Status: {1}, Location: {2}".format(self.sid, self.status, self.location))

    def print_dataset(self):
        print("Data: {0} = {1}".format(self.datatype, self.data))

    def print_packet(self):
        print("Packet ID: {0}, Timestamp: {1}, Auditee: {2}".format(self.pid, self.timestamp, self.get_auditee()))


class FishingNet(object):
    def __init__(self, rate):
        self.pid = 0
        self.rate = rate
        self.packets = []
        self.auditeeList = []

        self.group = self.rate * 2 - 1  # Each group in FNT contains (rate * 2 - 1) packets.
        self.countInitial = math.comb(self.rate + 1, 2)  # Counting nodes in the initial network

        edges = []  # Special nodes on the edge of the initial network.
        for n in range(1, self.rate):
            upper = int(n * (n + 1) / 2)
            lower = upper + n
            edges.append(upper)
            edges.append(lower)
        self.bound = edges

    def new_packet(self, timestamp, sid, status, location, datatype, data):  # Create a new packet.

        if self.pid == 0:  # First packet #0.
            packet = Packet(self.pid, timestamp, sid, status, location, datatype, data, None, None)

