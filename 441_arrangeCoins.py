"""
Arranging Coins
题目描述：
	You have a total of n coins that you want to form in
a staircase shape, where every k-th row must have exactly
k coins.
	Given n, find the total number of full staircase rows
that can be formed.
	n is a non-negative integer and fits within the range
of a 32-bit signed integer.

Example 1:
	n = 5
	The coins can form the following rows:
	¤
	¤ ¤
	¤ ¤
	Because the 3rd row is incomplete, we return 2.

Example 2:
	n = 8
	The coins can form the following rows:
	¤
	¤ ¤
	¤ ¤ ¤
	¤ ¤
	Because the 4th row is incomplete, we return 3.
"""
# 方法一
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1

        while n >= 0:
            n -= k
            k += 1

        return k - 2



# 方法二
import math
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((-1+math.sqrt(8*n+1))/2)
