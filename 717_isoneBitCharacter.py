"""
1-bit and 2-bit Characters
题目描述：
		We have two special characters. The first character can
e represented by one bit 0. The second character can be
represented by two bits (10 or 11).
	Now given a string represented by several bits. Return
whether the last character must be a one-bit character or not.
The given string will always end with a zero.
Example 1:
	Input:  [1,0,0]
	Output: True
	Explanation:The only way to decode it is two-bit character
and one-bit character. So the last character is one-bit character
Example 2:
	Input:  [1,1,1,0]
	Output: False
	Explanation:The only way to decode it is two-bit character
and two-bit character. So the last character is NOT one-bit
character.
Note:
	 1.1 <= len(bits) <= 1000.
	 2.bits[i] is always 0 or 1.
"""
# 比较慢的方法
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits:
        	return False
        n = len(bits)

        index = 0
        while index < n:
        	if index == n-1 :
        		return True
        	#当前位为1时，后移两位
        	if bits[index] == 1:
        		index += 2
        	#当前位为0时，后移1位
        	else:
        		index += 1
        return False
# 速度较快：只要1的个数为奇数个，就返回False；偶数个就True
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        length = len(bits)
        if(length == 1):
            return True
        else:
            howManyOnes = 0
            pointer = length - 2
            while(bits[pointer] == 1 and pointer >= 0):
                howManyOnes += 1
                pointer -= 1

            if(howManyOnes % 2 == 1):
                return False
            else:
                return True
