# -*- coding:utf-8 -*-


# English:
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
# As a reminder, a binary search tree is a tree that satisfies these constraints:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8] Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# Example 2:
# Input: root = [0,null,1] Output: [1,null,1]
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -104 <= Node.val <= 104
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.
# Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
#
# 中文:
# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
# 提醒一下，二叉搜索树满足下列约束条件：
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
# 注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同
# 示例 1：
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8] 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 示例 2：
# 输入：root = [0,null,1] 输出：[1,null,1]
# 示例 3：
# 输入：root = [1,0,2] 输出：[3,3,2]
# 示例 4：
# 输入：root = [3,2,4,1] 输出：[7,9,4,10]
# 提示：
# 树中的节点数介于 0 和 104 之间。
# 每个节点的值介于 -104 和 104 之间。
# 树中的所有值 互不相同 。
# 给定的树为二叉搜索树。


#
# @lc app=leetcode.cn id=538 lang=python
#
# [538] 把二叉搜索树转换为累加树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    count = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        self.convertBST(root.right)
        root.val += self.count
        self.count = root.val
        self.convertBST(root.left)
        return root

