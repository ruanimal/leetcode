# -*- coding:utf-8 -*-


# English:
# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9 Output: true
# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28 Output: false
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105
#
# 中文:
# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# 示例 1：
# 输入: root = [5,3,6,2,4,null,7], k = 9 输出: true
# 示例 2：
# 输入: root = [5,3,6,2,4,null,7], k = 28 输出: false
# 提示:
# 二叉树的节点个数的范围是  [1, 104].
# -104 <= Node.val <= 104
# root 为二叉搜索树
# -105 <= k <= 105


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



