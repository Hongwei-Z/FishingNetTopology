import FNT
from datetime import datetime

fnt = FNT.FishingNet(10)
for i in range(80):
    fnt.new_packet(datetime.now().strftime("%x"), "S1", "On", "HFX", "Tem", 18)

fnt.detach_packet(56)
fnt.display_packet(56)
fnt.display_fnt()