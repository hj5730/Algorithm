import sys

n = int(sys.stdin.readline())
my_card = set(map(int, sys.stdin.readline().split()[:n]))

m = int(sys.stdin.readline())
check_card = list(map(int, sys.stdin.readline().split()[:m]))

for check_num in check_card:
	if check_num in my_card:
		print(1, end=' ')
	else:
		print(0, end=' ')
