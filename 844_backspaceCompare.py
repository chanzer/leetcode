"""
Backspace String Compare
题目描述：
	Given two strings S and T, return if they are equal when
both are typed into empty text editors. # means a backspace
character.

Example 1:
	Input: S = "ab#c", T = "ad#c"
	Output:true
	Explanation:Both S and T become "ac".

Example 2:
	Input:  S = "ab##", T = "c#d#"
	Output:true
	Explanation:Both S and T become "".

"""
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
