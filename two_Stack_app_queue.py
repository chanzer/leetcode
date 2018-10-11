"""
两个栈实现一个队列

题目描述：
	用两个栈来实现一个队列，完成队列的Push和Pop操作。队列中的元素
	为int类型。
思路：
	由于队列是先进先出的，而栈是后进先出的，所以要用2个栈来实现队
	列的入队出队功能，队列的入队功能与栈的一样，出队时，先将第一个
	栈中的元素全部弹出，并倒入第二个栈中，将第二个栈中的栈顶元素弹
	出，并将stack2中剩下的元素倒回stack1中，即实现一次出队。
"""
class Solution:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
	def push(self,node):
		self.stack1.append(node)
	def pop(self):
		if self.stack2 == []:
			return self.stack2.pop()
		elif not self.stack1:
			return None
		else:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
			return self.stack2.pop()
