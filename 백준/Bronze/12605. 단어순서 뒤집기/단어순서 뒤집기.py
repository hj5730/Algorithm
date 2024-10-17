n = int(input())
result = []

for _ in range(n):
	wordList = str(input()).split(" ")
	reverseList = []

	for i in range(len(wordList)-1, -1, -1):
		reverseList.append(wordList[i])

	result.append((' '.join(reverseList)))

for idx in range(len(result)):
	print(f"Case #{idx+1}: {result[idx]}")
