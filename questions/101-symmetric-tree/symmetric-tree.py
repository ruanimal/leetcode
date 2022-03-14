# -*- coding:utf-8 -*-


# English:
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Example 1:
# Input: root = [1,2,2,3,4,4,3] Output: true
# Example 2:
# Input: root = [1,2,2,null,3,null,3] Output: false
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
# Follow up: Could you solve it both recursively and iteratively?
#
# 中文:
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 示例 1：
# 输入：root = [1,2,2,3,4,4,3] 输出：true
# 示例 2：
# 输入：root = [1,2,2,null,3,null,3] 输出：false
# 提示：
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？


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

