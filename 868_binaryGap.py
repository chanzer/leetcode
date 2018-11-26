"""
Binary Gap
题目描述：
	Given a positive integer N, find and return the longest
distance between two consecutive 1's in the binary representation
of N.
	If there aren't two consecutive 1's, return 0.


Example 1:
	Input:  22
	Output: 2
	Explanation:22 in binary is 0b10110.
	In the binary representation of 22, there are three ones,
and two consecutive pairs of 1's.
	The first consecutive pair of 1's have distance 2.
	The second consecutive pair of 1's have distance 1.
	The answer is the largest of these two distances, which is 2.


Example 2:
	Input:  5
	Output: 2
	Explanation:5 in binary is 0b101.

Note: 1 <= N <= 10^9
"""
# 方法一
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        index = []
        for i, num in enumerate(bin(N)):
            if num == '1':
                index.append(i)
        if len(index) == 1:
            return 0
        return max([index[i+1]-index[i] for i in range(len(index)-1)])

# 方法二
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = [i for i in range(32) if (N>>i) &1]
        if len(nums) < 2:
            return 0
        return max(nums[i+1] - nums[i] for i in range(len(nums)-1))

