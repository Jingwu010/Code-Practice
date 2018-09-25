def checkAP(numList):
	d = numList[1] - numList[0]
	for i in range(1, len(numList)):
		if numList[i] - numList[i - 1] != d:
			return False
	return True

if __name__ == '__main__':
	while True:
		try:
			n = input()
			numList = input()
			numList = numList.split()
			numList = [int(x) for x in numList]
			if checkAP(numList):
				print(2 * numList[-1] - numList[-2])
			else:
				print(numList[-1])
		except EOFError:
			break