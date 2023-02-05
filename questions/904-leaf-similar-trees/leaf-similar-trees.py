# -*- coding:utf-8 -*-

# <SUBID:18309052,UPDATE:20230205>
# English:
# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
# Example 1:
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8] Output: true
# Example 2:
# Input: root1 = [1,2,3], root2 = [1,3,2] Output: false
# Constraints:
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
#
# 中文:
# 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
# 举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。
# 如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
# 如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
# 示例 1：
# 输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8] 输出：true
# 示例 2：
# 输入：root1 = [1,2,3], root2 = [1,3,2] 输出：false
# 提示：
# 给定的两棵树结点数在 [1, 200] 范围内
# 给定的两棵树上的值在 [0, 200] 范围内


#
# @lc app=leetcode.cn id=872 lang=python
#
# [872] 叶子相似的树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def find_leaf(node, leafs=None):
            if leafs is None:
                leafs = []
            if not node.left and not node.right:
                leafs.append(node.val)
                return leafs
            if node.left:
                find_leaf(node.left, leafs)
            if node.right:
                find_leaf(node.right, leafs)
            return leafs
        return find_leaf(root1) == find_leaf(root2)


