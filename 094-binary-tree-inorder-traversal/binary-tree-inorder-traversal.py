# -*- coding:utf-8 -*-


# English:
# Given a binary tree, return the inorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3] 1 \ 2 / 3 Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
# 中文:
# 给定一个二叉树，返回它的中序 遍历。
# 示例:
# 输入: [1,null,2,3] 1 \ 2 / 3 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (66.43%)
# Likes:    226
# Dislikes: 0
# Total Accepted:    41.5K
# Total Submissions: 62.5K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [1,3,2]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # # v1 recurse version
        # if not root:
        #     return []
        # if not root.right and not root.left:
        #     return [root.val]

        # left = self.inorderTraversal(root.left) if root.left else []
        # right = self.inorderTraversal(root.right) if root.right else []
        # return left + [root.val] + right

        # # v2 loop version
        if not root:
            return []

        ans = []
        stack = [(1, root)]
        while stack:
            state, node = stack.pop()
            if state == 0:
                ans.append(node.val)
                continue

            if node.right:
                stack.append((1, node.right))
            stack.append((0, node))
            if node.left:
                stack.append(( 1, node.left))
        return ans

