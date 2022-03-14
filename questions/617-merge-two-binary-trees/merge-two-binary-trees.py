# -*- coding:utf-8 -*-


# English:
# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.
# Example 1:
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] Output: [3,4,5,5,4,null,7]
# Example 2:
# Input: root1 = [1], root2 = [1,2] Output: [2,2]
# Constraints:
# The number of nodes in both trees is in the range [0, 2000].
# -104 <= Node.val <= 104
#
# 中文:
# 给你两棵二叉树： root1 和 root2 。
# 想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。
# 返回合并后的二叉树。
# 注意: 合并过程必须从两个树的根节点开始。
# 示例 1：
# 输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] 输出：[3,4,5,5,4,null,7]
# 示例 2：
# 输入：root1 = [1], root2 = [1,2] 输出：[2,2]
# 提示：
# 两棵树中的节点数目在范围 [0, 2000] 内
# -104 <= Node.val <= 104


#
# @lc app=leetcode.cn id=617 lang=python
#
# [617] 合并二叉树
#
# https://leetcode-cn.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (68.10%)
# Total Accepted:    9.3K
# Total Submissions: 13.4K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL
# 的节点将直接作为新二叉树的节点。
#
# 示例 1:
#
#
# 输入:
# Tree 1                     Tree 2
# ⁠         1                         2
# ⁠        / \                       / \
# ⁠       3   2                     1   3
# ⁠      /                           \   \
# ⁠     5                             4   7
# 输出:
# 合并后的树:
# 3
# / \
# 4   5
# / \   \
# 5   4   7
#
#
# 注意: 合并必须从两个树的根节点开始。
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


