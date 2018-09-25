def checkQP(inputStr):
	inputStr = inputStr.strip("0")
	if inputStr == inputStr[::-1]:
		return "YES"
	else:
		return "NO"


if __name__ == '__main__':
	while True:
		try:
			inputStr = input()
			print(checkQP(inputStr))
		except EOFError:
			break