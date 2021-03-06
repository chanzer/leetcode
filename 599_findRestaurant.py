"""
Minimum Index Sum of Two Lits
题目描述：
		Suppose Andy and Doris want to choose a restaurant
for dinner,and they both have a list of favorite restaurants
represented by strings.
		You need to help them find out their common interest
with the least list index sum. If there is a choice tie
between answers,output all of them with no order requirement
You could assume there always exists an answer.

Example 1:
	Input: ["Shogun", "Tapioca Express", "Burger King", "KFC"]
           ["Piatti", "The Grill at Torrey Pines",
            "Hungry Hunter Steakhouse", "Shogun"]
	Output: ["Shogun"]
	Explanation:
	The only restaurant they both like is "Shogun".

Example 2:
	Input: ["Shogun", "Tapioca Express", "Burger King", "KFC"]
           ["KFC", "Shogun", "Burger King"]
	Output: ["Shogun"]
	Explanation:
	The restaurant they both like and have the least index sum
	is "Shogun" with index sum 1 (0+1).
Note:
	1.The length of both lists will be in the range of [1, 1000].
	2.The length of strings in both lists will be in the range of [1, 30].
	3.The index is starting from 0 to the list length minus 1.
	4.No duplicates in both lists.
"""
class Solution:
	def findRestaurant(self,list1,list2):
		"""
		:type List1:List[str]
		:type List2:List[str]
		:rtype :List[str]
		"""
		list1_index = {u:i for i,u in enumerate(list1)}
		best,res = 1e9,[]

		for j,v in enumerate(list2):
			i = list1_index.get(v,1e9)
			if i + j < best:
				best = i + j
				res = [v]
			elif i + j == best:
				res.append(v)
		return res


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        for i,r in enumerate(list1):
            d[r] = i
        res = []
        iSumMin = len(list1)+len(list2)-2
        for i,r in enumerate(list2):
            if r in d:
                iSum = i + d[r]
                if iSum < iSumMin:
                    res = [r]
                    iSumMin = iSum
                elif iSum == iSumMin:
                    res.append(r)
        return res
