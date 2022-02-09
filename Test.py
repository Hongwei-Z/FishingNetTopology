# Sample Test File

import FNT
import Visualization
import secrets


rate = 10
nodes = 90

f = FNT.FishingNet(rate)
for i in range(nodes):
    f.nextNode(secrets.token_hex(16))
f.toString()

