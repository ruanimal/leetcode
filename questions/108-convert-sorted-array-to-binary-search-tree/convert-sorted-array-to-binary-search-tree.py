# -*- coding:utf-8 -*-


# English:
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example:
# Given the sorted array: [-10,-3,0,5,9], One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST: 0 / \ -3 9 / / -10 5
#
# 中文:
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 示例:
# 给定有序数组: [-10,-3,0,5,9], 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树： 0 / \ -3 9 / / -10 5


#
# @lc app=leetcode.cn id=108 lang=python
#
# [108] 将有序数组转换为二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # # 比较慢， 存在对象的复制
        # if not nums:
        #     return
        # mid = len(nums) // 2
        # node = TreeNode(nums[mid])
        # node.left = self.sortedArrayToBST(nums[:mid])
        # node.right = self.sortedArrayToBST(nums[mid+1:])
        # return node

        def to_bst(nums, start, end):
            if start > end:
                return None
            mid = (start+end)//2
            node = TreeNode(nums[mid])
            node.left = to_bst(nums, start, mid-1)
            node.right = to_bst(nums, mid+1,end)
            return node
        return to_bst(nums, 0, len(nums) - 1)


