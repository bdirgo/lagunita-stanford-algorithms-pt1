import math

file = open('integerArray.txt', 'r')
# file = open('test.txt', 'r')
listOfNums = []
for line in file:
	listOfNums.append(int(line))

def mergeAndCountSplitInv(B, C, D):
	i = 0
	j = 0
	total = 0
	b = len(B)
	c = len(C)
	d = len(D)
	# print("B (mcs)", B)
	# print("C (mcs)", C)
	# print("D (mcs)", D)
	for k in range(d):
		if i == b:
			D[k] = C[j]
			j = j + 1
		elif j == c:
			D[k] = B[i]
			i = i + 1
		elif B[i] < C[j]:
			D[k] = B[i]
			i = i + 1
		elif C[j] < B[i]:
			D[k] = C[j]
			j = j + 1
			total += len(B[i:])
	# 	print("D[k]", D[k])

	# print("D (mcs)", D)
	# print("total", total)

	return total

def split(inputList):
	iLen = len(inputList)
	midpoint = iLen // 2
	return inputList[:midpoint], inputList[midpoint:]


def sortAndCount(A):
	# print("A", A)
	n = len(A)
	if n <= 1:
		return 0
	else:
		B, C = split(A)
		D = A
		# print("B (sc)", B)
		x = sortAndCount(B)
		# print("C (sc)", C)
		y = sortAndCount(C)
		z = mergeAndCountSplitInv(B, C, D)
		# print("D (sc)", D)
	return x + y + z

print(sortAndCount(listOfNums))
