import FNTClass

f = FNTClass.FishingNet(6)
for i in range(100):
    f.nextNode("Data", "Time")
f.printFNT()