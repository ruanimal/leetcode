# -*- coding:utf-8 -*-


# English:
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
#
# Example 1:
# Input: matrix = [   [1,2,3,4],   [5,1,2,3],   [9,5,1,2] ] Output: True Explanation: In the above grid, the diagonals are: "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]". In each diagonal all elements are the same, so the answer is True.
# Example 2:
# Input: matrix = [   [1,2],   [2,2] ] Output: False Explanation: The diagonal "[1, 2]" has different elements.
#
# Note:
# matrix will be a 2D array of integers.
# matrix will have a number of rows and columns in range [1, 20].
# matrix[i][j] will be integers in range [0, 99].
#
# Follow up:
# What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
# What if the matrix is so large that you can only load up a partial row into the memory at once?
#
# 中文:
# 如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。
# 给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。
# 示例 1:
# 输入: matrix = [   [1,2,3,4],   [5,1,2,3],   [9,5,1,2] ] 输出: True 解释: 在上述矩阵中, 其对角线为: "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。 各条对角线上的所有元素均相同, 因此答案是True。
# 示例 2:
# 输入: matrix = [   [1,2],   [2,2] ] 输出: False 解释: 对角线"[1, 2]"上的元素不同。
# 说明:
# matrix 是一个包含整数的二维数组。
# matrix 的行数和列数均在 [1, 20]范围内。
# matrix[i][j] 包含的整数在 [0, 99]范围内。
# 进阶:
# 如果矩阵存储在磁盘上，并且磁盘内存是有限的，因此一次最多只能将一行矩阵加载到内存中，该怎么办？
# 如果矩阵太大以至于只能一次将部分行加载到内存中，该怎么办？


#
# @lc app=leetcode.cn id=766 lang=python
#
# [766] 扁平化多级双向链表
#
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        ans = []
        for x in range(len(matrix)):
            tmp = set()
            y = 0
            while x < len(matrix) and y < len(matrix[0]):
                tmp.add(matrix[x][y])
                x += 1
                y += 1
                if len(tmp) != 1:
                    return False
            ans.append(tmp)
        for y in range(len(matrix[0])):
            tmp = set()
            x = 0
            # print('++')
            while x < len(matrix) and y < len(matrix[0]):
                # print(x, y)
                tmp.add(matrix[x][y])
                x += 1
                y += 1
                if len(tmp) != 1:
                    return False
            ans.append(tmp)
        return all(len(i)==1 for i in ans)

if __name__ == "__main__":
    s = Solution().isToeplitzMatrix([
        [1,2,3,4],
        [5,1,2,3],
        [9,5,1,2]
    ])
    print(s)

