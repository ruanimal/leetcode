# -*- coding:utf-8 -*-


# English:
# Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.
# Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
# Example 1:
# Input: root = [1,0,2], low = 1, high = 2 Output: [1,null,2]
# Example 2:
# Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3 Output: [3,2,null,1]
# Constraints:
# The number of nodes in the tree in the range [1, 104].
# 0 <= Node.val <= 104
# The value of each node in the tree is unique.
# root is guaranteed to be a valid binary search tree.
# 0 <= low <= high <= 104
#
# 中文:
# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。
# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。
# 示例 1：
# 输入：root = [1,0,2], low = 1, high = 2 输出：[1,null,2]
# 示例 2：
# 输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3 输出：[3,2,null,1]
# 提示：
# 树中节点数在范围 [1, 104] 内
# 0 <= Node.val <= 104
# 树中每个节点的值都是 唯一 的
# 题目数据保证输入是一棵有效的二叉搜索树
# 0 <= low <= high <= 104


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



