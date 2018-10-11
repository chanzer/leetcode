"""
整数中1出现的次数

题目描述：
	求出1~13的整数中1出现的次数，并算出100~1300的整数中1出现的次数？
	为此特别数了一下 1~13中包含1的数字有1，10，11，12，13，因此出现
	了6次，打比赛对于后面问题就没辙了。
	ACMer希望你帮帮他，并把问题更加普遍化，可以很快的求出任意非负整数
	区间中1出现的次数（从1到n中1出现的次数）
"""

# 方法一：数字换成字符型，判断每个元素中是不是有1（偷懒型）
class Solution:
	def NumberOf1Between1AndN_Solution(self,n):
		if n < 1 :
			return 0
		a = map(str,rang(n+1))
		ones = [i for i in a if '1' in i]
		return ''.join(ones).count('1')

#方法二：
