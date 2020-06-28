"""
3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。

给定一个由整数组成的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。

 

示例：

输入: [[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]]
输出: 1
解释:
下面的子矩阵是一个 3 x 3 的幻方：
438
951
276

而这一个不是：
384
519
762

总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
提示:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/magic-squares-in-grid
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        if (nrow<3) or (ncol<3):
            return 0

        def judge(r, c):
            num = [grid[i][j] for i in range(r-1,r+2) for j in range(c-1,c+2)]
            if len(set(num)) !=9:
                return False
            if any([(i>9) or(i<1) for i in num ]):
                return False
            num1 = grid[r-1][c-1] + grid[r+1][c+1] + grid[r][c]
            num2 = grid[r-1][c] + grid[r+1][c]+ grid[r][c]
            num3 = grid[r-1][c+1] + grid[r+1][c-1]+ grid[r][c]
            num4 = grid[r][c-1] + grid[r][c+1]+ grid[r][c]
            num5 = grid[r-1][c-1] + grid[r-1][c] +grid[r-1][c+1]
            num6 = grid[r+1][c-1] + grid[r+1][c] +grid[r+1][c+1]
            num7 = grid[r-1][c-1] + grid[r][c-1] + grid[r+1][c-1]
            num8 = grid[r-1][c+1] + grid[r][c+1] + grid[r+1][c+1]
            return num1==num2==num3==num4==num5==num6==num7==num8

        counter = 0
        for i in range(1,nrow-1):
            for j in range(1, ncol-1):
                if judge(i,j):
                    counter+=1
        return counter