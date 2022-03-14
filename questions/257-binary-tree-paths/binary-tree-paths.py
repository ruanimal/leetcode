# -*- coding:utf-8 -*-


# English:
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.
# Example 1:
# Input: root = [1,2,3,null,5] Output: ["1->2->5","1->3"]
# Example 2:
# Input: root = [1] Output: ["1"]
# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
#
# 中文:
# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 叶子节点 是指没有子节点的节点。
# 示例 1：
# 输入：root = [1,2,3,null,5] 输出：["1->2->5","1->3"]
# 示例 2：
# 输入：root = [1] 输出：["1"]
# 提示：
# 树中节点的数目在范围 [1, 100] 内
# -100 <= Node.val <= 100


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


