"""
Remove element

题目描述：
	给定一个数组nums和一个值val，你需要原地移除所有值等于val的元素，
	返回移除后数组的新长度。
	不要使用额外的数组空间，你必须在原地修改输入数组并在使用O(1)额外
	空间的条件下完成。
	元素的顺序可以改变。你不需要考虑数组总超出新长度后面的元素。
"""
class Solution:
	"""Remove element"""
	def removeElement(self,nums,val):
		nums[:] = [x for x in nums  if x != val]
		return len(nums)
