"""
旋转数组的最小数字

题目描述：
	把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的
	旋转。输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素
	例如：数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值
	为1。NOTE:给出的所有元素都大于0，若数组大小为0，请返回0。
"""
# 方法一：偷懒版
class Solution:
	def minNumberInRotateArray(self,rotateArray):
		if len(rotateArray) == 0:
			return '0'
		return min(rotateArray)
"""
方法二：二分查找
	思路：首先所给的旋转数组中局部有序，这完全可以想到二分查找来
	解决。设置三个指针，left,right,mid。当mid>=left时说明最小数
	在右边；当mid<=right时说明在左边。但是当left==right==mid时，
	就不能判断了，只能顺序查找。
"""

def minNumberInRotateArray(rotateArray):
	left = 0 #左侧的指针
	right = len(rotateArray) #右侧的指针
	mid = 0 #中间的指针
	while rotateArray[left] >= rotateArray[right-1]:
		#当两个指针走到挨着时即,right-left =1,right即为最小
		if right - left ==1:
			mid = right
			break
		mid = left + (int)((right-left)/2)
		#若mid=left=right
		if rotateArray[left]==rotateArray[mid] and rotateArray[right]==rotateArray[mid]:
			return minInorder(rotateArray,left,right)
		#若mid>left,则最小数在mid的右边，让left走到mid的位置
		if rotateArray[mid] >= rotateArray[left]:
			left =mid
		#若mid <right,则最小数在mid的左边,让right到mid的位置
		elif rotateArray[mid] < rotateArray[right-1]:
			right =mid
	return rotateArray[mid]

#顺序查找数组中的最小值
def minInorder(rotateArray,left,right):
	minNum = rotateArray[left]
	length = right - left
	for i in rang(length):
		if rotateArray[left+i] < minNum:
			minNum = rotateArray[left+i]
	return minNum
if __name__ == '__main__':
	array = [5,6,7,8,3,4]
	print(minNumberInRotateArray(array))
