# -*- coding:utf-8 -*-


# English:
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.
# Example:
# Given binary tree [3,9,20,null,null,15,7],
# 3 / \ 9 20 / \ 15 7
# return its depth = 3.
#
# 中文:
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 3 / \ 9 20 / \ 15 7
# 返回它的最大深度 3 。


#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


