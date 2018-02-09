class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        """

        First Solution(does not work) Greedy:
        sort the coins and pick the greatest coin and redo the rest
        does not work (only work when coins can construct each other)

        Second Solution (does not work) dfs:
        scan the coin list, and pick one coin add to largest possible amount
        then redo the same step for leftamount, for each amount, pick the smallest
        does not work because we dont know what amount of money will we pick
        (not the more the better)

        Third Solution (work but need to consider time complexity)
        For each amount of money, construct possible combination with fewest coins
        F(m) = F(m - c) + 1 (for each c in coins)

        """

        def dfs(coins, amount):
        	if amount == 0:
        		return 0
        	result = float('inf')
        	for coin in coins:
        		moneyleft = amount
        		nums = 0
        		flag = False
        		if moneyleft >= coin:
        			# print(coin, moneyleft)
        			nums += 1
        			moneyleft = moneyleft - coin

        			k = dfs(coins, moneyleft)
        			if k != -1:
        				nums += k
        				flag = True
        		if flag:
        			# print("..", result, nums)
        			result = min(result, nums)
        	if result == float('inf') or result == -1:
        		return -1
        	else: return result

        coins.sort(reverse = True)
        return dfs(coins, amount)
        # result = float('inf')
        # for coin in coins:
        # 	moneyleft = amount
	       #  nums = 0
        # 	if moneyleft >= coin:
        # 		# print(coin, moneyleft)
        # 		nums += moneyleft // coin
        # 		moneyleft = moneyleft % coin
        		
	       #  	if moneyleft == 0:
		      #   	result = min(result, nums + count)
		      #   	print("result = ",  result)
		      #   	continue

		      #   k = self.coinChange(coins, moneyleft, nums)
		      #   if k != -1:
			     #    nums += k
        # 	# print(coin, moneyleft)
        # if result == float('inf'):
        # 	return -1
        # else: return result

# print(Solution().coinChange([1,2,5], 11))

# print(Solution().coinChange([], 11))
# print(Solution().coinChange([2], 11))
# print(Solution().coinChange([2], 10))
print(Solution().coinChange([186,419,83,408], 6249))
# print(Solution().coinChange([499,498,497,3], 1500))
# print(Solution().coinChange([499,498,490,7,3], 1500))
# print(Solution().coinChange([499,498,480,17,5,3], 1500))
# print(Solution().coinChange([599,598,480,13,5,1], 1500))
print(Solution().coinChange([600,350,100,1], 1500))


