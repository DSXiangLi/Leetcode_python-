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
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alpha ={}

        for i in s:
            if i not in alpha:
                alpha[i]=1
            else:
                alpha[i] +=1

        for j in t:
            if j not in alpha:
                return False
            elif alpha[j] <=0:
                return False
            else:
                alpha[j] -=1
        return True

