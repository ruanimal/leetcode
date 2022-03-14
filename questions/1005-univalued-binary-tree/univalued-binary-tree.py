# -*- coding:utf-8 -*-


# English:
# A binary tree is uni-valued if every node in the tree has the same value.
# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
# Example 1:
# Input: root = [1,1,1,1,1,null,1] Output: true
# Example 2:
# Input: root = [2,2,2,5,2] Output: false
# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val < 100
#
# 中文:
# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。
# 示例 1：
# 输入：[1,1,1,1,1,null,1] 输出：true
# 示例 2：
# 输入：[2,2,2,5,2] 输出：false
# 提示：
# 给定树的节点数范围是 [1, 100]。
# 每个节点的值都是整数，范围为 [0, 99] 。


#
# @lc app=leetcode.cn id=965 lang=python
#
# [965] 独特的电子邮件地址
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root, pre=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if pre is not None and pre != root.val:
            # print(repr(pre), repr(root.val))
            return False
        pre = root.val
        left_is = self.isUnivalTree(root.left, pre)
        right_is = self.isUnivalTree(root.right, pre)
        return left_is and right_is



