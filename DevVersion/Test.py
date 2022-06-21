import FNT
from datetime import datetime

fnt = FNT.FishingNet(10)
# timestamp, sid, status, location, datatype, data
for i in range(150):
    fnt.new_packet(datetime.now().strftime("%x"), "S1", "On", "HFX", "Tem", 18)

fnt.display_fnt()
# pid, timestamp, sid, status, location, datatype, data, auditee1, auditee2