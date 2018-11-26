"""
Valid Perfect Square
题目描述：
	Given a positive integer num, write a function which
returns True if num is a perfect square else False.

Example 1:
	Input:  16
	Output: true

Example 2:
	Input: 14
	Output:false
"""
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return int(num ** 0.5) ** 2 == num

