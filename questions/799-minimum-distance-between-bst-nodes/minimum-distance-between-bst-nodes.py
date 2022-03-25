# -*- coding:utf-8 -*-

# <SUBID:16529211,UPDATE:20220325>
# English:
# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
# Example 1:
# Input: root = [4,2,6,1,3] Output: 1
# Example 2:
# Input: root = [1,0,48,null,null,12,49] Output: 1
# Constraints:
# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 105
# Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
#
# 中文:
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 差值是一个正数，其数值等于两值之差的绝对值。
# 示例 1：
# 输入：root = [4,2,6,1,3] 输出：1
# 示例 2：
# 输入：root = [1,0,48,null,null,12,49] 输出：1
# 提示：
# 树中节点的数目范围是 [2, 100]
# 0 <= Node.val <= 105
# 注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同


#
# @lc app=leetcode.cn id=783 lang=python
#
# [783] 二叉搜索树中的搜索
#
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (51.02%)
# Total Accepted:    2.3K
# Total Submissions: 4.5K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# 给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。
#
# 示例：
#
#
# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树结点对象(TreeNode object)，而不是数组。
#
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
#
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \
# ⁠   1   3
#
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
#
# 注意：
#
#
# 二叉树的大小范围在 2 到 100。
# 二叉树总是有效的，每个节点的值都是整数，且不重复。
#
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def tree_max(node):
            if node.right is None:
                return node.val
            m = tree_max(node.right)
            return m

        def tree_min(node):
            if node.left is None:
                return node.val
            m = tree_min(node.left)
            return m

        level = [root]
        min_abs = None
        while level:
            next_level = []
            for node in level:
                if not node.right and not node.left:
                    continue
                elif node.right and node.left:
                    next_level.append(node.right)
                    next_level.append(node.left)
                    node_abs = min(abs(node.val - tree_min(node.right)), abs(node.val - tree_max(node.left)))
                elif node.right:
                    next_level.append(node.right)
                    node_abs = abs(node.val - tree_min(node.right))
                else:
                    next_level.append(node.left)
                    node_abs = abs(node.val - tree_max(node.left))

                if min_abs is None:
                    min_abs = node_abs
                else:
                    min_abs = min(min_abs, node_abs)
            level = next_level
        return min_abs


