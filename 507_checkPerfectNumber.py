"""
Perfect Number
题目描述：
	We define the Perfect Number is a positive integer
that is equal to the sum of all its positive divisors except
itself.
	Now, given an integer n, write a function that returns
true when it is a perfect number and false when it is not.

Example:
	Input:28
	Output:True
	Explanation:28=1+2+4+7+14
"""
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in (6, 28, 496, 8128, 33550336)

import math
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        sq = int(math.sqrt(num))
        s = 1
        for d in range(2, sq + 1):
            if num % d == 0:
                s += d
                s+= int(num / d)

        return s == num
