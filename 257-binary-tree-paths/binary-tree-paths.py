# -*- coding:utf-8 -*-


# English:
# Given a binary tree, return all root-to-leaf paths.
# Note: A leaf is a node with no children.
# Example:
# Input: 1 / \ 2 3 \ 5 Output: ["1->2->5", "1->3"] Explanation: All root-to-leaf paths are: 1->2->5, 1->3
#
# 中文:
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 说明: 叶子节点是指没有子节点的节点。
# 示例:
# 输入: 1 / \ 2 3 \ 5 输出: ["1->2->5", "1->3"] 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3


#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        def dfs(node, path=None):
            if path is None:
                path = []
            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append('->'.join(path))
                return
            if node.left:
                dfs(node.left, path)
                path.pop()
            if node.right:
                dfs(node.right, path)
                path.pop()

        if not root:
            return
        dfs(root)
        return ans


