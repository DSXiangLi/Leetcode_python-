"""
慢慢码系列 - Leetcode Python

242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_s = dict()
        hash_t = dict()

        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]] +=1
            else:
                hash_s[s[i]] =1

        for i in range(len(t)):
            if t[i] in hash_t:
                hash_t[t[i]] +=1
            else:
                hash_t[t[i]] = 1

        return hash_t == hash_s

def main():

    s = input("Sting S: ")
    t = input("String t: ")

    result = Solution().isAnagram(s,t)

    print("S and t are Anagram: ",result)