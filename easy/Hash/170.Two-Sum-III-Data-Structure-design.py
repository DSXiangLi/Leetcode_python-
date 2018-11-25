"""
慢慢码系列 - Leetcode Python

170. Two Sum III - Data Structure design [Class Design] [Hash Table]

Design and implement a TwoSum class. It should support the following
operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false

"""

import collections

class TwoSum1(object):
    """
    方法1.用Hash存储数据， 每次查找遍历Hash
    add O(1)
    find O(N)
    """
    def __init__(self):
        self.target = None
        self.hash_table = collections.defaultdict(int) # set default value for missing key

    def add(self, num):
        self.hash_table[num] +=1  # use defaultdict(int) for counting

    def find(self, target):
        for key in list(self.hash_table.keys()):
            if (target - key) in self.hash_table:
                return True

        return False

class TwoSum2(object):
    """
    方法2.直接存储两个数的和
    add O(N)
    find O(1)
    """
    def __init__(self):
        self.target = None
        self.hash_sum = collections.defaultdict(int)
        self.nums = []

    def add(self, num):
        for i in self.nums:
            self.hash_sum[i + num] +=1
        self.nums.append(num)

    def find(self, target):
        if target in self.hash_sum:
            return True
        else:
            return False


def main():
    twosum = TwoSum1()
    twosum.add(1)
    twosum.add(3)
    twosum.add(5)

    print('find(4) -> ', twosum.find(4))
    print('find(7) -> ', twosum.find(7))

    twosum = TwoSum2()
    twosum.add(1)
    twosum.add(3)
    twosum.add(5)

    print('find(4) -> ', twosum.find(4))
    print('find(7) -> ', twosum.find(7))


