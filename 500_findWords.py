"""
Keyboard Row
题目描述：
		Given a List of words, return the words that can be
typed using letters of alphabet on only one row's of American
keyboard like the image below.

Example:
	Input:  ["Hello", "Alaska", "Dad", "Peace"]
	Output: ["Alaska", "Dad"]

Note:
	1.You may use one character in the keyboard more than once
	2.You may assume the input string will only contain letters
of alphabet.
"""
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        ans=[]
        for word in words:
        	#str.lower() 方法转换字符串中所有大写字符为小写
            t=set(word.lower())
            if a & t == t:
                ans.append(word)
            if b & t == t:
                ans.append(word)
            if c & t == t:
                ans.append(word)
        return ans
