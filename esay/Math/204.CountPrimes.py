'''
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.
'''

'''
Optimized version
No need to iterate the number bigger than root(n). 
Except for looping, use iterable list to solve this problem 
'''

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        if a number cannot be decomposed by 2 non-negative then it is a prime 
        '''
        if n <3:
            return 0
        flag = [True] * n
        flag[0] = False # 0 is not prime
        flag[1] = False # 1 is not prime
        for i in range(2, int(math.sqrt(n)+1) ):
            if flag[i] == True:
                flag[i*i:n:i] = [False] * int((n-i*i-1)/i+1) 
            
        return sum(flag)
		
'''
My first solution. very very slow 
'''
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        if a number cannot be decomposed by 2 non-negative then it is a prime 
        '''
        if n <3:
            return 0
        flag = [True] * n
        flag[0] =  flag[1]= False # 0and 1 are not prime 
        for i in range(2,n-1):
            if flag[i]== True:
                for j in range(i,int((n-1)/i+1) ):
                    flag[i*j] = False # flag all number that contain i as not prime
        return sum(flag)
	
