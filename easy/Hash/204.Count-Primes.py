"""
慢慢码系列 - Leetcode Python

204. Count Primes [Array][Hash Table]

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

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

def main():
    Input = input('Input n : ')
    Input = int(Input)

    result = Solution2().countPrimes(Input)

    print("There are {} prime number <= {}".format(result, Input))