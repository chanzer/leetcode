"""
Longest Harmonious Subsequence
题目描述：
		We define a harmonious array is an array where the
difference between its maximum value and its minimum value
is exactly 1.
		Now, given an integer array, you need to find the
length of its longest harmonious subsequence among all its
possible subsequences.

Example 1:
	Input:  [1,3,2,2,5,2,3,7]
	Output: 5
	Explanation:
	The longest harmonious subsequence is [3,2,2,2,3]

Note:
	The length of the input array will not exceed 20,000.
"""
from collections import Counter
class Solution:
	def findLHS(self,nums):
		"""
		:type nums:List[int]
		:rtype : int
		"""
		count = Counter(nums)
		res = 0
		for i in count:
			if i+1 in count:
				res = max(res,count[i]+count[i+1])
		return res


class Solution:
	def findLHS(self,nums):
		"""
		:type nums:List[int]
		:rtype : int
		"""
		mp = {}
		for i in nums:
			if i not in mp:
				mp[i] = 1
			else:
				mp[i] += 1

		res = 0
		for i in mp:
			if mp.get(i+1):
				res = max(res,mp[i]+mp[i+1])
		return res
