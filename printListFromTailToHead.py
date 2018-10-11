"""
倒序输出链表

题目描述：
	输入一个链表，按链表值从尾到头的顺序返回一个ArrayList.
"""
class Solution:
	def printListFromTailToHead(self,listNode):
		if listNode == listNode:
			return []
		else:
			return self.printListFromTailToHead(listNode.next)+[listNode.val]

