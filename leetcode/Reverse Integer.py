"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        _flag = False
        if x < 0:
        	_flag = True
        	x = -x
        xStr = str(x)
        rxStr = xStr[::-1]
        rx = int(rxStr)
        limites = 1 << 31
        if _flag == False and rx <= (limites - 1):
        	return rx
        elif _flag == True and rx <= (limites):
        	return -rx
        else:
        	return 0

if __name__ == '__main__':
	s = Solution()
	print(s.reverse(123))
	print(s.reverse(-123))
	print(s.reverse(1000000003))
	print(s.reverse(10))
	print(s.reverse(100))
	print(s.reverse(1463847412))
	print(s.reverse(9000000))
	print(s.reverse(1534236469))
	print(s.reverse(-2147483648))
	print(s.reverse(000))
	print(s.reverse(0))