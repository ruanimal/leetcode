# -*- coding:utf-8 -*-


# English:
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 1 / \ 2 2 / \ / \ 3 4 4 3
# But the following [1,2,2,null,3,null,3] is not:
# 1 / \ 2 2 \ \ 3 3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#
# 中文:
# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 1 / \ 2 2 / \ / \ 3 4 4 3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 1 / \ 2 2 \ \ 3 3
# 说明:
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。


#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (44.77%)
# Total Accepted:    27.3K
# Total Submissions: 59.6K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        level = [root]
        while level:
            next_level = []
            for node in level:
                if not node:
                    continue
                next_level.append(node.left)
                next_level.append(node.right)
            if next_level:
                for i in range(len(next_level)//2):
                    a = next_level[i].val if next_level[i] else None
                    b = next_level[-i-1].val if next_level[-i-1] else None
                    if a != b:
                        return False
            level = next_level
        return True

