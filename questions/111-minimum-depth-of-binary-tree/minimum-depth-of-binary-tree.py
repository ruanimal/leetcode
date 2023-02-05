# -*- coding:utf-8 -*-

# <SUBID:16413091,UPDATE:20230205>
# English:
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
# Example 1:
# Input: root = [3,9,20,null,null,15,7] Output: 2
# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6] Output: 5
# Constraints:
# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000
#
# 中文:
# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明：叶子节点是指没有子节点的节点。
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7] 输出：2
# 示例 2：
# 输入：root = [2,null,3,null,4,null,5,null,6] 输出：5
# 提示：
# 树中节点数的范围在 [0, 105] 内
# -1000 <= Node.val <= 1000


#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (36.82%)
# Total Accepted:    14.4K
# Total Submissions: 37.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最小深度  2.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        if (root.left == None and root.right == None):
            return 1
        if (root.left == None):
            return 1 + self.minDepth(root.right)
        if (root.right == None):
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


