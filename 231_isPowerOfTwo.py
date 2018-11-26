"""
Power of Two
题目描述：
	Given an integer, write a function to determine if
it is a power of two.

Example 1:
	Input:  1
	Output: true
    Explanation: 2**0 = 1

Example 2:
	Input: 16
	Output:true
    Explanation:2**4 = 16

Example 3:
    Input: 218
    Output:false
"""

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return False
        while n & 1 == 0:
            # x >> 1：把x右移1位，相当于除以2
            n >> 1
        return n == 1
