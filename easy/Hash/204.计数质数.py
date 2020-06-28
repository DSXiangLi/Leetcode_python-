"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""

## Run Time Error O(N*K)
##store all found prime number, for each new number see if it can be divided by any prime number
class Solution1:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <=2:
            return 0
        count = 1
        primes = dict()
        primes[2] = 1
        for i in range(2,n):
            prime_flag = True
            for k in list(primes.keys()):
                if i%k==0:
                    prime_flag = False
                    break
            if prime_flag:
                primes[i] = 1
                count +=1
        return count

## Success O(N)
## once we know N is prime,  than 2N,3N... can't be prime
## and we when come to b, and b is still flaged as prime, then repeat above
class Solution2:
    def countPrimes(self, n):
        """
        type n: int
        rtype: int
        """
        if n <=2:
            return 0
        primes = [1] * (n-1)
        primes[:1] = [0,0]
        for i in range(2, int(n**0.5+1) ):
            if primes[i] == 1:
                primes[(i*i):n:i] = [0] * int( (n-1-i*i)//i +1)

        return sum(primes)


class Solution:
    def countPrimes(self, n: int) -> int:
        import numpy as np
        is_prime = np.ones(n)
        is_prime[:2] = 0
        for i in range(2, (n+1)//2):
            # 小于i^2的在前一次遍历(i-1)的时候已经遍历
            # 只遍历n/2之前的
            is_prime[i**2:n:i] = 0

        return int(sum(is_prime))

def main():
    Input = input('Input n : ')
    Input = int(Input)

    result = Solution2().countPrimes(Input)

    print("There are {} prime number <= {}".format(result, Input))