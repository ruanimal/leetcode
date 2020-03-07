# -*- coding:utf-8 -*-


# English:
# Given an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
# Follow up:
# Recursive solution is trivial, could you do it iteratively?
# Example 1:
# Input: root = [1,null,3,2,4,null,5,6] Output: [1,3,5,6,2,4]
# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
# Constraints:
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]
#
# 中文:
# 给定一个 N 叉树，返回其节点值的前序遍历。
# 例如，给定一个 3叉树 :
# 返回其前序遍历: [1,3,5,6,2,4]。
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?


#
# @lc app=leetcode.cn id=589 lang=python
#
# [589] N-ary Tree Preorder Traversal
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root, ret=None):
        """
        :type root: Node
        :rtype: List[int]
        """
        if ret is None:
            ret = []
        if not root:
            return
        ret.append(root.val)
        for i in root.children:
            self.preorder(i, ret)
        return ret


