import sys

def solve():
	n = int(sys.stdin.readline())
	my_card = list(map(int, sys.stdin.readline().split()))

	m = int(sys.stdin.readline())
	check_card = list(map(int, sys.stdin.readline().split()))

	result = {}
	for check_num in set(check_card):
		result[check_num] = 0

	for my_num in my_card:
		if my_num in result:
			result[my_num] += 1

	for check_num in check_card:
		print(result[check_num], end=' ')

solve()