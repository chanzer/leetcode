"""
Two sum

题目描述：
	给定一个整数数组和一个目标值，找出数组中和为目标值的两个数
	你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

"""
class Solution:
	"""两数之和"""
	def twosum(self,nums,target):
		l = len(nums)
		for i in range(l):
			for j in range(i+1,l):
				if nums[i]+nums[j] == target:
					return [i,j]

# 更快更强
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        placeHolder = {}
        for i, x in enumerate(nums):
            if target - x in placeHolder:
                return placeHolder[target - x], i
            placeHolder[x] = i
