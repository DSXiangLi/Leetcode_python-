"""
慢慢码系列 - Leetcode Python

290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

"""
## Solution1 and Solution has same Run time O(N). Solution 1 use less space

## Solution1. use 1 hash table. If the string is very long, solution shold be faster
class Solution1:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(" ")

        hash_table = dict()

        if len(pattern) != len(str_list):
            return False
        for i in range(len(pattern)):

            if pattern[i] not in hash_table:
                if  str_list[i] in hash_table.values():
                    return False
                else:
                    hash_table[pattern[i]] = str_list[i]
            else:
                if hash_table[pattern[i]] != str_list[i]:
                    return False
        return True

# Solution2: 2 hash table. O(N).
class Solution2:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(" ")

        hash_pattern = dict()
        hash_string = dict()

        if len(pattern) != len(str_list):
            return False
        for i in range(len(pattern)):
            print(hash_pattern)
            print(hash_string)
            if pattern[i] in hash_pattern:
                if (hash_pattern[pattern[i]] != str_list[i]) or hash_string[str_list[i]] != pattern[i] :
                    return False
            else:
                if str_list[i] in hash_string:
                    return False
                else:
                    hash_pattern[pattern[i]] = str_list[i]
                    hash_string[str_list[i]] = pattern[i]
        return True

# Solution: a concise version of 2 hash table solution. remove the one unnecesary condition - hash_string[str_list[i]] != pattern[i]
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(" ")

        hash_pattern = dict()
        hash_string = dict()

        if len(pattern) != len(str_list):
            return False
        for (pad, string) in zip(pattern, str_list):
            if pad not in hash_pattern:
                if string in hash_string:
                    return False
                else:
                    hash_pattern[pad], hash_string[string] = string, pad
            else:
                if hash_pattern[pad] != string:
                    return False
        return True

def main():
    pattern = input("Input Pattern here: ")
    string = input("Input String here: ")

    result = Solution().wordPattern(pattern, string)

    print("Whether String follows pattern: ", result )