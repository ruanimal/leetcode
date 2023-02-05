# -*- coding:utf-8 -*-

# <SUBID:17816632,UPDATE:20230205>
# English:
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
# Example 1:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15 Output: 32 Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10 Output: 23 Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
# Constraints:
# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.
#
# 中文:
# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
# 示例 1：
# 输入：root = [10,5,15,3,7,null,18], low = 7, high = 15 输出：32
# 示例 2：
# 输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10 输出：23
# 提示：
# 树中节点数目在范围 [1, 2 * 104] 内
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# 所有 Node.val 互不相同


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0 
        res = 0
        if L <= root.val <= R:
            res += root.val
        if root.val > L:
            res += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            res += self.rangeSumBST(root.right, L, R)
        return res
