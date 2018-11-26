"""
Long Pressed Name
题目描述：
	Your friend is typing his name into a keyboard.  Sometimes,
when typing a character c, the key might get long pressed, and
the character will be typed 1 or more times.
	You examine the typed characters of the keyboard.  Return
True if it is possible that it was your friends name, with some
characters (possibly none) being long pressed.

Example 1:
	Input: name = "alex", typed = "aaleex"
	Output:true
	Explanation:'a' and 'e' in 'alex' were long pressed.

Example 2:
	Input: name = "saeed", typed = "ssaaedd"
	Output:false
	Explanation:'e' must have been pressed twice, but it wasn't
	            in the typed output.
"""
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        n = len(name)
        i = 0
        for letter in typed:
            if i < n and letter == name[i]:
                i += 1
            elif 1 <= i <= n and letter == name[i-1]:
                continue
            else:
                return False

        return i == n
