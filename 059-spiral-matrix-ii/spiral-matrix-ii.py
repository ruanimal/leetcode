# -*- coding:utf-8 -*-


# English:
# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
# Example:
# Input: 3 Output: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
#
# 中文:
# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 示例:
# 输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]


#
# @lc app=leetcode.cn id=59 lang=python
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (72.48%)
# Likes:    104
# Dislikes: 0
# Total Accepted:    10.9K
# Total Submissions: 14.9K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0 for _ in range(n)] for _ in range(n)]
        pos = [0, -1]
        heads = [
            (1, 1),
            (0, 1),
            (1, -1),
            (0, -1),
        ]
        head = heads[0]
        next_head = lambda h: heads[(heads.index(h)+1) % 4]
        for i in range(1, n**2+1):
            pos[head[0]] += head[1]
            if pos[0] >= n or pos[1] >= n or pos[0] < 0 or pos[1] < 0 or ans[pos[0]][pos[1]]:
                pos[head[0]] -= head[1]
                head = next_head(head)
                pos[head[0]] += head[1]
            ans[pos[0]][pos[1]] = i
        return ans

if __name__ == "__main__":
    s = Solution().generateMatrix(3)
    print(s)
    s = Solution().generateMatrix(0)
    print(s)
    s = Solution().generateMatrix(2)
    print(s)

