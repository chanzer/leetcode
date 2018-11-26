"""
Intersection of Two Linked Lists
题目描述：
	Write a program to find the node at which the intersection
of two singly linked lists begins.
	For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

	begin to intersect at node c1.

Note:
	1.If the two linked lists have no intersection at all,
	  return null.
	2.The linked lists must retain their original
	  structure after the function returns.
	3.You may assume there are no cycles anywhere in
	  the entire linked structure.
	4.Your code should preferably run in O(n) time
	  and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            if pa:
                pa = pa.next
            else:
                pa = headB
            if pb:
                pb = pb.next
            else:
                pb = headA
        return pa


