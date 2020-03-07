# -*- coding:utf-8 -*-


# English:
# Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
# Example 1:
#
# Input: 1 / \ 0 2 L = 1 R = 2 Output: 1 \ 2
# Example 2:
#
# Input: 3 / \ 0 4 \ 2 / 1 L = 1 R = 3 Output: 3 / 2 / 1
#
# 中文:
# 给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
# 示例 1:
# 输入: 1 / \ 0 2 L = 1 R = 2 输出: 1 \ 2
# 示例 2:
# 输入: 3 / \ 0 4 \ 2 / 1 L = 1 R = 3 输出: 3 / 2 / 1


#
# @lc app=leetcode.cn id=669 lang=python
#
# [669] 修剪二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root



