import FNT

s = FNT.Sensor("S1", "01", "Halifax")
d = FNT.Dataset("Temperature", "18")

packet = FNT.Packet(0, 1653510171, "0", "0", s.sid, s.status, s.location, d.datatype, d.data)
packet.print_packet()
