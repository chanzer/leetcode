"""
链表中环的入口节点

题目描述：
		给一个链表，若其中包含环，请找出该链表的环的入口节点
		否则输出null
思路：
	遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点

"""

class Solution:
	def EntryNodeOfLoop(self,pHead):
		res = []
		p = pHead
		while p:
			if p in res:
				return p
			else:
				res.append(p)
			p = p.next
