# Sample Test File

import FNT
import Visualization
import secrets


rate = 10
nodes = 66

f = FNT.FishingNet(rate)
for i in range(nodes):
    f.new_node(secrets.token_hex(16))

f.toString()
print(f.tip_list)

#Visualization.draw_FNT(10, 1000)

