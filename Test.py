# Sample Test File

import FNT
import Visualization
import secrets


rate = 10
nodes = 16

f = FNT.FishingNet(rate)
for i in range(nodes):
    f.new_node(secrets.token_hex(16))

f.toString()

#Visualization.draw_FNT(rate, nodes)
