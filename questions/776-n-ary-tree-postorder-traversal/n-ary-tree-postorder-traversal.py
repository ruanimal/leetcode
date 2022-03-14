# -*- coding:utf-8 -*-


# English:
# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
# Example 1:
# Input: root = [1,null,3,2,4,null,5,6] Output: [5,6,3,2,4,1]
# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# 0 <= Node.val <= 104
# The height of the n-ary tree is less than or equal to 1000.
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
# 中文:
# 给定一个 n 叉树的根节点
# root ，返回 其节点值的 后序遍历 。
# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
# 示例 1：
# 输入：root = [1,null,3,2,4,null,5,6] 输出：[5,6,3,2,4,1]
# 示例 2：
# 输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] 输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]
# 提示：
# 节点总数在范围 [0, 104] 内
# 0 <= Node.val <= 104
# n 叉树的高度小于或等于 1000
# 进阶：递归法很简单，你可以使用迭代法完成此题吗?


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


