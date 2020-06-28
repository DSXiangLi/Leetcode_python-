"""

包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:

输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0pr
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0

"""


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        nrows = len( M )
        ncols = len( M[0] )
        new_M = [[0] * ncols for i in range( nrows )]
        for r in range( nrows ):
            for c in range( ncols ):
                up = max( 0, r - 1 )
                down = min( nrows - 1, r + 1 )
                left = max( 0, c - 1 )
                right = min( ncols - 1, c + 1 )

                new_M[r][c] = int(
                    sum( [M[i][j] for i in range( up, down + 1 ) for j in range( left, right + 1 )] ) / (
                                (right - left + 1) * (
                                down - up + 1)) )

        return new_M

