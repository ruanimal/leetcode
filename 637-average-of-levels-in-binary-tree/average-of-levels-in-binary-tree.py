# -*- coding:utf-8 -*-


# English:
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
#
# Input: 3 / \ 9 20 / \ 15 7 Output: [3, 14.5, 11] Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
#
# The range of node's value is in the range of 32-bit signed integer.
#
# 中文:
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
# 示例 1:
# 输入: 3 / \ 9 20 / \ 15 7 输出: [3, 14.5, 11] 解释: 第0层的平均值是 3, 第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
# 注意：
# 节点值的范围在32位有符号整数范围内。


#
# @lc app=leetcode.cn id=637 lang=python
#
# [637] 二叉树的层平均值
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        level = [root]
        while level:
            next_level = []
            tmp = 0.0
            for i in level:
                tmp += i.val
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            ans.append(tmp/len(level))
            level = next_level
        return ans



