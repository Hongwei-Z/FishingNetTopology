import FNT

f = FNT.FishingNet(6)
for i in range(100):
    f.next_node("Data", "Time")
f.print_fnt()
print()
f.find_node(10)
print()
f.disable_node(60)
f.print_fnt()
print()
f.find_tips(30)
print()
f.find_approver(10)
print()
f.find_node(10)
