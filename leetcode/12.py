"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {1000: "M", 900:"CM", 500:"D", 400:"CD",
        				100:"C", 90:"XC", 50:"L", 40:"XL",
        					10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        roman_list = sorted(roman_dict.keys(), reverse=True)
        roman_str = ""
        for value in roman_list:
        	while num >= value:
        		num -= value
        		roman_str += roman_dict[value]
        return roman_str

if __name__ == '__main__':
	s = Solution()
	print(s.intToRoman(312))
	print(s.intToRoman(3999))
	print(s.intToRoman(4))
	print(s.intToRoman(1))
	print(s.intToRoman(10))
	print(s.intToRoman(1998))
	print(s.intToRoman(1001))