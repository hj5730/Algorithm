import sys

def solve():
	n = int(sys.stdin.readline())
	my_card = list(map(int, sys.stdin.readline().split()))

	m = int(sys.stdin.readline())
	check_card = list(map(int, sys.stdin.readline().split()))

	result = {}
	for my_num in my_card:
		if my_num in result:
			result[my_num] += 1
		else:
			result[my_num] = 1

	for check_num in check_card:
		if check_num in result:
			print(result[check_num], end=' ')
		else:
			print(0, end=' ')

solve()