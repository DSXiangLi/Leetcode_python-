'''
566. Reshape the Matrix
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
'''

## O(n) space O(n) time
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r*c:
            return nums
        else:
            newnums = []
            ncol = 0
            nrow = 0 
            row = []
            for i in range(len(nums)):
                for j in range(len(nums[0])):
                    ncol +=1
                    row.append(nums[i][j])      
                    if ncol==c:
                        newnums.append(row)
                        row = []
                        ncol = 0
                        nrow +=1
            return newnums
			
## O(n) time, O(n) space 
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r*c:
            return nums
        else:
            onerow = [nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
        
            return[ onerow[row*c: (row+1)*c] for row in range(r) ]