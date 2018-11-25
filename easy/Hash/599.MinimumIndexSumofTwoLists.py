"""
慢慢码系列 - Leetcode Python

599. Minimum Index Sum of Two Lists

Suppose Andy and Doris want to choose a restaurant for dinner,
and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum.
If there is a choice tie between answers,
 output all of them with no order requirement.
 You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""
## 和find cycle 问题类似这里也是用连个指针当快指针到达末尾时慢指针刚好的中间

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hash1 = {choice:index for index,choice in enumerate(list1)}
        hash2 = {choice:(index + hash1[choice]) for index,choice in enumerate(list2) if choice in hash1}
        min_index=  min(hash2.values())

        return [for key,value in hash2.items() if value ==min_index]

