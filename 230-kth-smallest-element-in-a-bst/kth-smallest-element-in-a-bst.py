# -*- coding:utf-8 -*-


# English:
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# Example 1:
# Input: root = [3,1,4,null,2], k = 1 3 / \ 1 4 \   2 Output: 1
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3 5 / \ 3 6 / \ 2 4 / 1 Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#
# 中文:
# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
# 示例 1:
# 输入: root = [3,1,4,null,2], k = 1 3 / \ 1 4 \   2 输出: 1
# 示例 2:
# 输入: root = [5,3,6,2,4,null,null,1], k = 3 5 / \ 3 6 / \ 2 4 / 1 输出: 3
# 进阶：
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？


#
# @lc app=leetcode.cn id=230 lang=python
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (65.30%)
# Likes:    80
# Dislikes: 0
# Total Accepted:    15.9K
# Total Submissions: 24.3K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# 输出: 1
#
# 示例 2:
#
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# 输出: 3
#
# 进阶：
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def kthSmallest(self, root, k):
    #     """
    #     :type root: TreeNode
    #     :type k: int
    #     :rtype: int
    #     """
    #     v1 非递归中序排序
    #     if not root:
    #         return []

    #     ans = []
    #     stack = [(1, root)]
    #     while stack and len(ans)<k:
    #         state, node = stack.pop()
    #         if state == 0:
    #             ans.append(node.val)
    #             continue

    #         if node.right:
    #             stack.append((1, node.right))
    #         stack.append((0, node))
    #         if node.left:
    #             stack.append((1, node.left))
    #     return ans[-1] if len(ans) == k else None

    # def kthSmallest(self, root, k):
    #     """
    #     生成器法
    #     :type root: TreeNode
    #     :type k: int
    #     :rtype: int
    #     """

    #     def mid_order(root):
    #         if not root: return
    #         yield from mid_order(root.left)
    #         yield root.val
    #         yield from mid_order(root.right)

    #     ans = None
    #     gen = mid_order(root)
    #     for _ in range(k):
    #         ans = next(gen)
    #     return ans

    def kthSmallest(self, root, k):
        def inorder(root):
            if not root: return
            inorder(root.left)
            self.count -= 1
            if self.count == 0:
                self.res = root.val
                return
            inorder(root.right)

        self.res, self.count = None, k
        inorder(root)
        return self.res


