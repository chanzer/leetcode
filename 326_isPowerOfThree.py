"""
Power of Three
题目描述：
	Given an integer, write a function to determine if
it is a power of three.

Example 1:
	Input:  27
	Output: true

Example 2:
	Input: 0
	Output:false


Example 3:
    Input: 9
    Output:true
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 3^19 =1162261467  3^20 is bigger than int
        return n > 0 and (3^19) % n == 0


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while  n % 3 == 0:
            n = n / 3
        return n == 1
