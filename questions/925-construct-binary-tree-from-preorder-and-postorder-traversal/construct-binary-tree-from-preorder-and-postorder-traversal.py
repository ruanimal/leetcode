# -*- coding:utf-8 -*-

# <SUBID:283748920,UPDATE:20220325>
# English:
# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
# If there exist multiple answers, you can return any of them.
# Example 1:
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1] Output: [1,2,3,4,5,6,7]
# Example 2:
# Input: preorder = [1], postorder = [1] Output: [1]
# Constraints:
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
#
# 中文:
# 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。
# 如果存在多个答案，您可以返回其中 任何 一个。
# 示例 1：
# 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1] 输出：[1,2,3,4,5,6,7]
# 示例 2:
# 输入: preorder = [1], postorder = [1] 输出: [1]
# 提示：
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# preorder 中所有值都 不同
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# postorder 中所有值都 不同
# 保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

try:
    from comm import *
except ImportError:
    LOCAL_TEST = False

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(postorder) == 0:
            return

        self.postorder_index = {i[1]:i[0] for i in enumerate(postorder)}
        self.preorder_index = {i[1]:i[0] for i in enumerate(preorder)}
        return self.helper(preorder, postorder, 0, len(preorder)-1, 0, len(postorder)-1)

    def helper(self, preorder: List[int], postorder: List[int],
               pre_low, pre_high, post_low, post_high) -> TreeNode:
        if (pre_high - pre_low < 0):
            return
        if pre_low == pre_high:
            return TreeNode(preorder[pre_low])

        lroot_val = preorder[pre_low+1]
        rroot_val = postorder[post_high-1]
        root = TreeNode(preorder[pre_low])
        root.left = self.helper(preorder, postorder,
                                pre_low+1, self.preorder_index[rroot_val]-1,
                                post_low, self.postorder_index[lroot_val])
        root.right = self.helper(preorder, postorder,
                                 self.preorder_index[rroot_val], pre_high,
                                 self.preorder_index[rroot_val]+1, post_high-1)
        return root

if LOCAL_TEST:
    s = Solution()
    s.constructFromPrePost(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1])


