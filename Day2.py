with open("inputFile.txt", "r") as f:
	data = [x for x in f.read().split("\n")]

x = 0
y = 0
aim = 0
for xx in data:

	xx = xx.split()
	if xx[0] == "forward":
		y += (aim*int(xx[1]))
		x += int(xx[1])
	elif xx[0] == "down":
		aim += int(xx[1])
	else:
		aim -= int(xx[1])

print(x,y,x*y)