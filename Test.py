# Sample Test File

import FNT
import secrets

f = FNT.FishingNet(10)
for i in range(16):
    f.new_node(secrets.token_hex(16))

f.toString()
