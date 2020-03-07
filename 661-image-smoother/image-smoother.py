# -*- coding:utf-8 -*-


# English:
# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.
# Example 1:
#
# Input: [[1,1,1], [1,0,1], [1,1,1]] Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]] Explanation: For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0 For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0 For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# Note:
#
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
#
# 中文:
# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。
# 示例 1:
# 输入: [[1,1,1], [1,0,1], [1,1,1]] 输出: [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 解释: 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
# 注意:
# 给定矩阵中的整数范围为 [0, 255]。
# 矩阵的长和宽的范围均为 [1, 150]。


#
# @lc app=leetcode.cn id=661 lang=python
#
# [661] 图片平滑器
#
# https://leetcode-cn.com/problems/image-smoother/description/
#
# algorithms
# Easy (45.82%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 6K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入)
# ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。
#
# 示例 1:
#
#
# 输入:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# 输出:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
#
#
# 注意:
#
#
# 给定矩阵中的整数范围为 [0, 255]。
# 矩阵的长和宽的范围均为 [1, 150]。
#
#
#
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        I = len(M)
        J = len(M[0])
        def get_avg(i, j):
            points = [
                (i-1, j-1),
                (i-1, j),
                (i-1, j+1),
                (i, j-1),
                (i, j),
                (i, j+1),
                (i+1, j-1),
                (i+1, j),
                (i+1, j+1),
            ]
            tmp = []
            for a, b in points:
                if 0 <= a < I and 0 <= b < J:
                    tmp.append(M[a][b])
            return sum(tmp)//len(tmp)

        ret = []
        for i in range(len(M)):
            ret.append([])
            for j in range(len(M[i])):
                tmp = get_avg(i, j)
                ret[i].append(tmp)
        return ret

if __name__ == "__main__":
    s = Solution().imageSmoother([[1,1,1],
    [1,0,1],
    [1,1,1]])
    print(s)


