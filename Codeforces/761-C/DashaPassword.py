import sys

class Status:
    def __init__(self, digit, char, special, step, token):
        self.digit = digit
        self.char = char
        self.special = special
        self.step = step
        update(token)

    def update(self, token):
    	if token - '0' >= 0 and token - '0' <= 9:
    		self.digit = True
    	elif token - 'a' >= 0 and token - 'a' <= 26:
    		self.char = True
    	elif token == '*' or token == '#' or token == '&':
    		self.special = True

valueTable = [[]]
tokens = [[]]

def initiateTable(rows, cols):
	global tokens
	global valueTable
	valueTable = [[Status() for j in range(cols)] for i in range(rows)]
	for i in range(rows):
		newStatus = status(False, False, False, 0, tokens[i][0])
		valueTable[i][0] = newStatus
		for j in range(1,cols/2):
			newStatus1 = status(False, False, False, j, tokens[i][j])
			valueTable[i][j] = newStatus1
			newStatus2 = status(False, False, False, j, tokens[i][clos-j])
			valueTable[i][clos-j] = newStatus2

def dpPassword(rows, cols):
	global tokens
	global valueTable
	for i in range(1, rows):
		for j in range(cols):
			for k in range(cols):
				status = valueTable[i-1][k]

def findSmallest(index, cols):
	global valueTable
	maxs = sys.maxsize
	smallest = [[[maxs * 2] * 2] * 2]
	for j in range(cols):
		for d in range(2):
			for c in range(2):
				for s in range(2):
					smallest[d][c][s] = min(smallest[d][c][s], valueTable[index][j][d][c][s])
	return smallest

def main():
	global tokens
	rows = input()
	cols = input()
	tokens = [[0 for j in range(cols)] for i in range(rows)]
	for i in range(rows):
		for j in range(cols):
			tokens[i][j] = input()
	initiateTable(rows, cols)
	dpPassword(rows, cols)



