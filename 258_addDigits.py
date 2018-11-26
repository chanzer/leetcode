"""
Add Digits
题目描述：
	Given a non-negative integer num, repeatedly add all
its digits until the result has only one digit.

Example :
	Input:  38
	Output: 2
    Explanation: The process is like: 3 + 8 = 11,1 + 1 = 2.
             Since 2 has only one digit, return it.
"""
# 方法一：转化为字符，每位相加
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = sum(map(int,str(num)))
        while res >= 10:
            res = sum(map(int,str(res)))
        return res
"""
方法二：
N=(a[0] * 1 + a[1] * 10 + ...a[n] * 10 ^n)
	and a[0]...a[n] are all between [0,9]

设：M = a[0] + a[1] + ..a[n]

1 % 9 = 1
10 % 9 = 1
100 % 9 = 1
N % 9 = a[0] + a[1] + ...+a[n]
---> N % 9 == M
---> N = M( % 9) 且 9 % 9 = 0
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = num % 9
        if num == 0:
            return 0
        if res == 0:
            return 9
        else:
            return res

