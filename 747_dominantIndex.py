"""
Largest Number At Least Twice of Others
题目描述：
		In a given integer array nums, there is always exactly
one largest element.
		Find whether the largest element in the array is at
least twice as much as every other number in the array.
		If it is, return the index of the largest element,
otherwise return -1.
Example 1:
	Input: nums = [3,6,1,0]
	Output: 1
	Explanation:6 is the largest integer, and for every other
number in the array x,6 is more than twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:
	Input:  nums = [1,2,3,4]
	Output: -1
	Explanation:4 isn't at least as big as twice the value of
3, so we return -1.
Note:
	 1.nums will have a length in the range [1, 50].
	 2.Every nums[i] will be an integer in the range [0, 99].
"""
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNumber = max(nums)
        """
        all(iterable)  --iterable元祖或列表
        如果iterable的所有元素都不为0、空、False 返回true
        否则返回False
        注意：空列表、空元祖返回True
        """
        if all(maxNumber >= 2*i for i in nums if i!= maxNumber):
            return nums.index(maxNumber)
        return -1

