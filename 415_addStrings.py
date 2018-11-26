"""
Add Strings
题目描述：
	Given two non-negative integers num1 and num2
represented  as string, return the sum of num1 and num2.


Note:
	1.The length of both num1 and num2 is < 5100.
	2.Both num1 and num2 contains only digits 0-9.
	3.Both num1 and num2 does not contain any leading zero.
	4.You must not use any built-in BigInteger library
or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i,j = len(num1)-1, len(num2)-1
        plus = 0
        ans = ''
        while i >= 0 or j >= 0 or plus:
            if i >= 0:
                plus += int(num1[i])
            if j >= 0:
                plus += int(num2[j])
            # %:取模，返回除法的余数
            ans = str(plus % 10) + ans
            i,j = i-1,j-1
            # //:整除，返回商的整数部分(向下取整)
            plus = plus // 10
        return ans

num1 = '11'
num2 = '34'
i,j = len(num1)-1, len(num2)-1
plus = 0
ans = ''
while i >= 0 or j >= 0 or plus:
    print('i:',i)
    print('j:',j)
    if i >= 0:
        plus += int(num1[i])
    if j >= 0:
        plus += int(num2[j])
    # %:取模，返回除法的余数
    ans = str(plus % 10) + ans
    print(ans)
    i,j = i-1,j-1
    # //:整除，返回商的整数部分(向下取整)
    plus = plus // 10


