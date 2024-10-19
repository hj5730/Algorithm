import sys
from collections import Counter

def solve():
	n = int(sys.stdin.readline())
	my_card = list(map(int, sys.stdin.readline().split()))

	m = int(sys.stdin.readline())
	check_card = list(map(int, sys.stdin.readline().split()))

	my_card_counter = dict(Counter(my_card))
	for check_num in check_card:
		if check_num in my_card_counter:
			print(my_card_counter[check_num], end=' ')
		else:
			print(0, end=' ')

solve()