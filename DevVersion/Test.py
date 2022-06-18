import FNT

s = FNT.Sensor("S1", "00", "Halifax")
d = FNT.Dataset("Temperature", "18")

a1 = FNT.Packet(1, 1653510171, s.sid, s.status, s.location, d.datatype, d.data, 0, 0)
a2 = FNT.Packet(2, 1653510171, s.sid, s.status, s.location, d.datatype, d.data, 0, 0)

packet = FNT.Packet(0, 1653510171, s.sid, s.status, s.location, d.datatype, d.data, a1, a2)

packet.print_sensor()
packet.print_dataset()
packet.print_packet()

# pid, timestamp, sid, status, location, datatype, data, auditee1, auditee2
# print(packet.get_pid())
# print(packet.get_timestamp())
# print(packet.get_auditee())
# print(packet.get_sid())
# print(packet.get_status())
# print(packet.get_location())
# print(packet.get_datatype())
# print(packet.get_data())