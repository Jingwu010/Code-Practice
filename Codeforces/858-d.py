def checkPB(numList):
	# at least O(n^2) time complexity
	for phoneNum in numList:
		# loop each phone num 70000
		# 0(n)
		loop_flag = True
		for length in range(1, len(phoneNum)+1):
			if loop_flag == False: break
			for startIndex in range(0, len(phoneNum)):
				# 9*9 = 81 looping times
				if loop_flag == False: break
				subStr = phoneNum[startIndex: startIndex + length]
				find_flag = True
				for otherPhoneNum in numList:
					# loop other phone num 70000
					# 0(n)
					if otherPhoneNum == phoneNum:
						continue
					if find_flag == False:
						break
					if subStr in otherPhoneNum:
						find_flag = False
				if find_flag == True:
					loop_flag = False
					print(subStr)


if __name__ == '__main__':
	while True:
		try:
			n = input()
			numList = []
			for i in range(int(n)):
				numList.append(input())
			checkPB(numList)
		except EOFError:
			break

"""
3
123456789
100000000
100123456

7
000
01
---------
4
123456789
193456789
134567819
934567891

2
193
13
91
---------
2
123456789
100000000

2
0
---------
2
123456789
123456781

9
81
---------
2
123456789
123654789

34
36
---------
"""





