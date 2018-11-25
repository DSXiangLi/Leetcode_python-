"""
慢慢码系列 - Leetcode Python

246. Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic.

The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""

## Trick 6 and 9 must be in symmetric position. 8 and 1 can be anywhere
## if num has (2K+1) digits then the number in the middle must be 8 or 1
class Solution1(object):
    def isStrobogrammatic(self, num):
        last = len(num)-1

        for i in range((len(num)//2) ):
            if not( (num[i] == num[last -i] and num[i] in ['0','1','8'])
                or (num[i] == '6' and num[last - i]== '9')
                or (num[last-i] =='6' and num[i] =='9') ):
                return False

        if (len(num)%2!=0) and (num[len(num)//2] not in ['0','1','8']):
            return False

        return True

## More concise way with hash table
class Solution2(object):
    def isStrobogrammatic(self, num):
        hash_table = {'0':'0','8':'8','1':'1','6':'9','9':'6'}

        length = len(num)

        for i in range((length//2)):
            if (num[i] not in hash_table) or (hash_table[num[i]] != num[length-1-i]):
                return False

        if (length%2!=0) and (num[length//2] not in ['0','1','8']):
            return False

        return True

def main():
    string = input('Input your number : ')

    result = Solution2().isStrobogrammatic(string)

    print("THe number is strobogrammatic: ",result)
