# Sample Test File

import FNT
import Visualization
import secrets


rate = 5
nodes = 60

f = FNT.FishingNet(rate)
for i in range(nodes):
    f.nextNode(secrets.token_hex(16))

f.toString()
print(f.tip_list)

Visualization.draw_FNT(rate, nodes)

