# -*- coding:utf-8 -*-


# English:
# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
# Example 1:
# Input: 5 / \ 3 6 / \ \ 2 4 7 Target = 9 Output: True
# Example 2:
# Input: 5 / \ 3 6 / \ \ 2 4 7 Target = 28 Output: False
#
# 中文:
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# 案例 1:
# 输入: 5 / \ 3 6 / \ \ 2 4 7 Target = 9 输出: True
# 案例 2:
# 输入: 5 / \ 3 6 / \ \ 2 4 7 Target = 28 输出: False


#
# @lc app=leetcode.cn id=653 lang=python
#
# [653] 两数之和 IV - 输入 BST
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return
            nodes_map[root.val] = id(root)
            dfs(root.left)
            dfs(root.right)

        nodes_map = {}
        dfs(root)
        for key, val in nodes_map.items():
            if (k - key) in nodes_map and nodes_map[k - key] != val:
                return True
        return False



