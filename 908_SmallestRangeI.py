"""
Smallest Range I
题目描述：
	Given an array A of integers, for each integer A[i] we may
choose any x with -K <= x <= K, and add x to A[i].
	After this process, we have some array B.
	Return the smallest possible difference between the maximum
value of B and the minimum value of B.


Example 1:
	Input:  A = [1], K = 0
	Output: 0
	Explanation:B = [1]

Example 2:
	Input:  A = [0,10], K = 2
	Output: 6
	Explanation:B = [2,8]

Note: 1. 1 <= A.length <= 1000
	  2. 0 <= A[i] <= 10000
	  3. 0 <= K <= 10000
"""
class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2*K)
