"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# use hash table to store positino of each character.
# check if the position list are the same
# Time O(N), memory O(N)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def str_replace(ss):
            num = 0
            numdict = {}
            new_ss = []
            for i in range( len( ss ) ):
                if ss[i] in numdict:
                    new_ss.append( numdict[ss[i]] )
                else:
                    numdict[ss[i]] = num
                    new_ss.append( num )
                    num += 1
            print( new_ss )
            return new_ss

        s = str_replace( s )
        t = str_replace( t )

        return s == t

)