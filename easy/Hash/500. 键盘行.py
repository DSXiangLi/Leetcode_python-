"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
示例：

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]

"""


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1, line2, line3 = set( 'qwertyuiop' ), set( 'asdfghjkl' ), set( 'zxcvbnm' )

        def judge(word):
            word = set( word.lower() )
            return (word.issubset( line1 )) or (word.issubset( line2 )) or (word.issubset( line3 ))

        return [word for word in words if judge( word )]