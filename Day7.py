''''
Day 7...'''
with open("Day7Input.txt", "r") as f:
	data = [int(x) for x in f.read().split("\n")]

l = len(data)
f = []

for v in range(l):
    f.append((sum([abs(x-v) for x in data])))
print(min(f))    



