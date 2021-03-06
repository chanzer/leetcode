"""
Happy Number
题目描述：
		Write an algorithm to determine if a number is "happy".
		A happy number is a number defined by the following
process: Starting with any positive integer, replace the number
by the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1. Those numbers
for which this process ends in 1 are happy numbers.

Example :
	Input:  19
	Output: True
	Explanation:1**2 + 9**2 = 82
				8**2 + 2**2 = 68
				6**2 + 8**2 = 100
				1**2 + 0**2 + 0**2 = 1

"""
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        old_list = []
        if n==1:
            return True
        while n not in old_list:
            old_list.append(n)
            n_str = list(str(n))
            n = sum([int(i) ** 2 for i in n_str])
            if n==1:
                return True
        return False

