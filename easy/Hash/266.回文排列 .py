"""
慢慢码系列 - Leetcode Python

246. Palindrom Permutation

Given a string, determine if apermutation of the string coudl form a palindrome

For example:
"code"-> False, "aab" -> True, 'carerac' -> True
"""
class Solution(object):
    def canPermutePalindrome(self, s):
        hash_table = dict()
        for i in range(len(s)):
            if (s[i] in hash_table):
                hash_table[s[i]] +=1
            else:
                hash_table[s[i]] = 1
        value_count = list(hash_table.values())

        odd_count = 0
        for i in range(len(value_count)):
            if value_count[i]%2==1:
                odd_count +=1

            if odd_count >1:
                return False

        return True

def main():
    string = input("Input String here :")

    result = Solution().canPermutePalindrome(string)

    print("Is it palindrom: ", result )
