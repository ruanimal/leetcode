# -*- coding:utf-8 -*-

# <SUBID:17657326,UPDATE:20220325>
# English:
# Given the root of a binary tree, invert the tree, and return its root.
# Example 1:
# Input: root = [4,2,7,1,3,6,9] Output: [4,7,2,9,6,3,1]
# Example 2:
# Input: root = [2,1,3] Output: [2,3,1]
# Example 3:
# Input: root = [] Output: []
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
# 中文:
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 示例 1：
# 输入：root = [4,2,7,1,3,6,9] 输出：[4,7,2,9,6,3,1]
# 示例 2：
# 输入：root = [2,1,3] 输出：[2,3,1]
# 示例 3：
# 输入：root = [] 输出：[]
# 提示：
# 树中节点数目范围在 [0, 100] 内
# -100 <= Node.val <= 100


#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        # tmp = root.left
        # root.left = self.invertTree(root.right)
        # root.right = self.invertTree(tmp)
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


