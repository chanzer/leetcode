"""
Sqrt(x)
题目描述：
	Implement int sqrt(int x).
	Compute and return the square root of x, where x is guaranteed
to be a non-negative integer.
	Since the return type is an integer, the decimal digits are
truncated and only the integer part of the result is returned.

Example 1:
	Input:  4
	Output: 2

Example 2:
	Input: 8
	Output:2
"""
# 方法一：
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x**0.5)

# 方法二：
import math
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))
