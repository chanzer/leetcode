"""
Count Primes质数/素数
题目描述：
		Count the number of prime numbers less than a
		non-negative number, n.

Example :
	Input:  10
	Output: 4
	Explanation:There are 4 prime numbers less than 10,
				they are 2, 3, 5, 7.
"""

class Solution:
    def countPrimes(self, n):
    	"""
    	:type n :int
    	:rtype :int
    	"""
        if n <= 2:
            return 0
        n_sqrt = int(n**0.5) + 1
        isPrime = [0, 0] + [1] * (n-2)

        for i in range(2, n_sqrt):
            if not (isPrime[i]):
                continue
            for j in range(i**2, n, i):
                isPrime[j] = 0

        return sum(isPrime)
