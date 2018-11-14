import math

# file = open('integerArray.txt', 'r')
file = open('test.txt', 'r')
listOfNums = []
for line in file:
	listOfNums.append(int(line))

def mergeAndCountSplitInv(B, C, D):

	i = 0
	j = 0
	total = 0
	b = len(B)
	c = len(C)
	print("B", B)
	print("C", C)
	for k in range(len(D)):
		# print("i", i)
		# print("j", j)

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
		print("D[k]", D[k])

	print("D", D)
	print("total", total)

	return total


def sortAndCount(A, n):
	print("A", A)
	l = math.floor(n / 2)
	if n == 1:
		return 0
	else:
		B = A[:l]
		C = A[l:]
		D = A
		print("B", B)
		print("C", C)

		x = sortAndCount(B, l)
		y = sortAndCount(C, l)
		z = mergeAndCountSplitInv(B, C, D)
		print("D", D)
	return x + y + z

print(sortAndCount(listOfNums, len(listOfNums)))
