import FNT

s = FNT.Sensor("S1", "01", "Halifax")
d = FNT.Dataset("Temperature", "18")

a1 = FNT.Packet(1, 1653510171, 0, 0, s.sid, s.status, s.location, d.datatype, d.data)
a2 = FNT.Packet(2, 1653510171, 0, 0, s.sid, s.status, s.location, d.datatype, d.data)

packet = FNT.Packet(0, 1653510171, a1, a2, s.sid, s.status, s.location, d.datatype, d.data)

packet.print_sensor()
packet.print_dataset()
packet.print_packet()

# pid, timestamp, auditee1, auditee2, sid, status, location, datatype, data
print(packet.get_pid())
print(packet.get_timestamp())
print(packet.get_auditee())
print(packet.get_sid())
print(packet.get_status())
print(packet.get_location())
print(packet.get_datatype())
print(packet.get_data())