import FNT

n = FNT.Node("1", "2")
s = FNT.Sensor("3", "4", "5")
d = FNT.Database("6", "7")
print("Packet:")
packet = FNT.Packet(n.nid, n.timestamp, s.sid, s.status, s.location, d.datatype, d.data)