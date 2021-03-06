"""
Missing Number
题目描述：
		Given a non-empty array of integers, return the
		third maximum number in this array. If it does not
		 exist, return the maximum number. The time
		 complexity must be in O(n).
Example 1:
	Input: [3,2,1]
	Output:1
Explanation:
	The third maximun is 1

Example 2:
	Input: [1,2]
	Output:2
Explanation:
	The third maximun does not exist,so the maximum (2)
	is returned instead.

Example 3:
	Input: [2,2,3,1]
	Output:1
Explanation:
	Note that the third maximun here means the third
	manimun distinct number.Both numbers with value 2
	are both considered as second maximum.
"""
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        if len(nums_set) < 3:
	        return max(nums_set)
        else:
	        return sorted(nums_set)[-3]
