# -*- coding:utf-8 -*-


# English:
# Given an n-ary tree, return the postorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
# Follow up:
# Recursive solution is trivial, could you do it iteratively?
# Example 1:
# Input: root = [1,null,3,2,4,null,5,6] Output: [5,6,3,2,4,1]
# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
# Constraints:
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]
#
# 中文:
# 给定一个 N 叉树，返回其节点值的后序遍历。
# 例如，给定一个 3叉树 :
# 返回其后序遍历: [5,6,3,2,4,1].
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?


#
# @lc app=leetcode.cn id=590 lang=python
#
# [590] N-ary Tree Postorder Traversal
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root, ret=None):
        """
        :type root: Node
        :rtype: List[int]
        """
        if ret is None:
            ret = []
        if not root:
            return
        for i in root.children:
            self.postorder(i, ret)
        ret.append(root.val)
        return ret


