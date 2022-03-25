# -*- coding:utf-8 -*-

# <SUBID:17940886,UPDATE:20220325>
# English:
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
# Example 1:
# Input: nums = [-10,-3,0,5,9] Output: [0,-3,9,-10,null,5] Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# Example 2:
# Input: nums = [1,3] Output: [3,1] Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.
#
# 中文:
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
# 示例 1：
# 输入：nums = [-10,-3,0,5,9] 输出：[0,-3,9,-10,null,5] 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
# 示例 2：
# 输入：nums = [1,3] 输出：[3,1] 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
# 提示：
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums 按 严格递增 顺序排列


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


