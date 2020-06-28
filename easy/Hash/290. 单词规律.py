"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split(' ')
        return list(map(pattern.index, pattern)) == list(map(str.index, str))