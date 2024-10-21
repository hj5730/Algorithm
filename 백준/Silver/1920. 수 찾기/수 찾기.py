import sys

n = int(sys.stdin.readline())
setA = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
checkList = list(map(int, sys.stdin.readline().split()))

for checkNum in checkList:
	if checkNum in setA:
		print(1)
	else:
		print(0)