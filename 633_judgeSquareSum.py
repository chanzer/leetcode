"""
Sum of Square Number
题目描述：
	Given a non-negative integer c, your task is to decide
whether there're two integers a and b such that
a^2 + b^2 = c.

Example 1:
	Input:5
	Output:True
	Explanation:1**2 + 2**2 =5

Example 2:
	Input:3
	Output:False
"""
import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        while i**2 <= c:
            j = math.sqrt(c - i**2)
            if j == int(j):
                return True
            i += 1
        return False
