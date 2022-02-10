# Sample Test File

import FNT
import Visualization
import secrets
from datetime import datetime


rate = 10
nodes = 100
time = datetime.now()

f = FNT.FishingNet(rate)
for i in range(nodes):
    f.nextNode(secrets.token_hex(16), time)
f.toString()

