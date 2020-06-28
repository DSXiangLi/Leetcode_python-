"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
 

限制：

0 <= s 的长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        if len(s)==0:
            return " "

        for i in s:
            dic[i] = dic.get(i,0) + 1

        # python 3.5+ only, the dict is ordered
        for key,val in dic.items():
            if val ==1:
                return key

        return " "