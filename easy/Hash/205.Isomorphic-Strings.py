"""
慢慢码系列 - Leetcode Python

205.Isomorphic Strings [Hash Table]

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

"""

# use hash table to store positino of each character.
# check if the position list are the same
# Time O(N), memory O(N)
class Solution1:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False

        hash_s = dict()
        hash_t = dict()

        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]].append(i)
            else:
                hash_s[s[i]] = [i]

        count_s = list(hash_s.values())

        for j in range(len(t)):
            if t[j] in hash_t:
                hash_t[t[j]].append(j)
            else:
                hash_t[t[j]] = [j]

        count_t = list(hash_t.values())

        if len(count_t)!= len(count_s):
            return False
        else:
            for i in range(len(count_s)) :
                if count_s[i] not in count_t:
                    return False

        return True

def main():
    s = input('Input first string: ')
    t = input('Input second string: ')

    result = Solution1().isIsomorphic(s, t)

    print(result)