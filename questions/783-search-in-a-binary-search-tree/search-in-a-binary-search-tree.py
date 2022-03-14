# -*- coding:utf-8 -*-


# English:
# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
# Example 1:
# Input: root = [4,2,7,1,3], val = 2 Output: [2,1,3]
# Example 2:
# Input: root = [4,2,7,1,3], val = 5 Output: []
# Constraints:
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107
#
# 中文:
# 给定二叉搜索树（BST）的根节点
# root 和一个整数值
# val。
# 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回
# null 。
# 示例 1:
# 输入：root = [4,2,7,1,3], val = 2 输出：[2,1,3]
# Example 2:
# 输入：root = [4,2,7,1,3], val = 5 输出：[]
# 提示：
# 数中节点数在 [1, 5000] 范围内
# 1 <= Node.val <= 107
# root 是二叉搜索树
# 1 <= val <= 107


#
# @lc app=leetcode.cn id=700 lang=python
#
# [700] Search in a Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return

        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return root


