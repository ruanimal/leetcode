# -*- coding:utf-8 -*-


# English:
# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
# Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.
# Example 1:
# Input: img = [[1,1,1],[1,0,1],[1,1,1]] Output: [[0,0,0],[0,0,0],[0,0,0]] Explanation: For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0 For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0 For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# Example 2:
# Input: img = [[100,200,100],[200,50,200],[100,200,100]] Output: [[137,141,137],[141,138,141],[137,141,137]] Explanation: For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137 For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141 For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
# Constraints:
# m == img.length
# n == img[i].length
# 1 <= m, n <= 200
# 0 <= img[i][j] <= 255
#
# 中文:
# 图像平滑器 是大小为 3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。
# 每个单元格的  平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。
# 如果一个单元格周围存在单元格缺失的情况，则计算平均灰度时不考虑缺失的单元格（即，需要计算红色平滑器中 4 个单元格的平均值）。
# 给你一个表示图像灰度的 m x n 整数矩阵 img ，返回对图像的每个单元格平滑处理后的图像 。
# 示例 1:
# 输入:img = [[1,1,1],[1,0,1],[1,1,1]] 输出:[[0, 0, 0],[0, 0, 0], [0, 0, 0]] 解释: 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
# 示例 2:
# 输入: img = [[100,200,100],[200,50,200],[100,200,100]] 输出: [[137,141,137],[141,138,141],[137,141,137]] 解释: 对于点 (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137 对于点 (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141 对于点 (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
# 提示:
# m == img.length
# n == img[i].length
# 1 <= m, n <= 200
# 0 <= img[i][j] <= 255


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


