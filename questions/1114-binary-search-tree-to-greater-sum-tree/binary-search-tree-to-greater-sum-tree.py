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
# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val <= 100
# All the values in the tree are unique.
# Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/
#
# 中文:
# 给定一个二叉搜索树
# root (BST)
# ，请将它的每个
# 节点
# 的值替换成树中大于或者等于该
# 节点
# 值的所有
# 节点
# 值之和。
# 提醒一下， 二叉搜索树 满足下列约束条件：
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
# 示例 1：
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8] 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 示例 2：
# 输入：root = [0,null,1] 输出：[1,null,1]
# 提示：
# 树中的节点数在 [1, 100] 范围内。
# 0 <= Node.val <= 100
# 树中的所有值均 不重复 。
# 注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/  相同


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.bstToGst(root.right)
        self.total += root.val
        root.val = self.total
        self.bstToGst(root.left)
        return root

