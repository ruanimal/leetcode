# -*- coding:utf-8 -*-

# <SUBID:23496029,UPDATE:20230205>
# English:
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
# Example 1:
# Input: root = [1,2,3,4,5] Output: 3 Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:
# Input: root = [1,2] Output: 1
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100
#
# 中文:
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
# 示例 :
# 给定二叉树
# 1 / \ 2 3 / \ 4 5
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
# 注意：两结点之间的路径长度是以它们之间边的数目表示。


#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
#
# https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (45.12%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 13.3K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
#
# 示例 :
# 给定二叉树
#
#
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \
# ⁠     4   5
#
#
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.ans = 0
        self.find_depth(root)
        return self.ans

    def find_depth(self, node):
        if not node.left and not node.right:
            return 0

        width = 0
        left_depth = 0
        right_depth = 0
        if node.left:
            left_depth = self.find_depth(node.left)   # 左子树深度
            width += left_depth + 1   # 左半路径长度
        if node.right:
            right_depth = self.find_depth(node.right)
            width += right_depth + 1
        self.ans = max(self.ans, width)
        return max(left_depth, right_depth) + 1   # 当前深度为子树深度的较大者, 再加一



