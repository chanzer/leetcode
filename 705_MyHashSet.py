"""
Design HashSet
题目描述：
		Design a HashSet without using any built-in hash
table libraries.
		To be specific, your design should include these
functions:
	1.add(value): Insert a value into the HashSet.
	2.contains(value) : Return whether the value
	  exists in the HashSet or not.
	3.remove(value): Remove a value in the HashSet.
	 If the value does not exist in the HashSet, do nothing.

Example 1:
	MyHashSet hashSet = new MyHashSet();
	hashSet.add(1);
	hashSet.add(2);
	hashSet.contains(1);  // returns true
	hashSet.contains(3);  // returns false (not found)
	hashSet.add(2);
	hashSet.contains(2);  // returns true
	hashSet.remove(2);
	hashSet.contains(2);  // returns false (already removed)
Note:
	1.All values will be in the range of [0, 1000000].
	2.The number of operations will be in the range of
	  [1, 10000].
	3.Please do not use the built-in HashSet library.
"""
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set=set()

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        try:
            self.set.remove(key)
        except:
            pass

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key not in self.set:
            return False
        else:
            return True

