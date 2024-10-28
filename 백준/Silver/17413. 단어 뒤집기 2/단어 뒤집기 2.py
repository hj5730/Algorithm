import sys

stack = []
sList = list(sys.stdin.readline().rstrip())


tag_flag = False
word = ''
for s in sList:
	if s == '<':
		tag_flag = True
		tag = '<'
		if len(word) != 0:
			stack.append(word)
			word = ''
	elif tag_flag == True:
		tag += s
		if s == '>':
			tag_flag = False
			word = ''
			stack.append(tag)
	else:
		word += s

if len(word) != 0:
	stack.append(word)

while len(stack) != 0:
	if '<' in stack[0]:
		print(stack.pop(0), end='')
	else:
		s_print = []
		for s_split in stack[0].split():
			s_print.append(s_split[::-1])
		print(' '.join(s_print), end='')
		stack.pop(0)