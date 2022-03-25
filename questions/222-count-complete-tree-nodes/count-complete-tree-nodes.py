# -*- coding:utf-8 -*-

# <SUBID:288945927,UPDATE:20220325>
# English:
# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# Design an algorithm that runs in less than O(n) time complexity.
# Example 1:
# Input: root = [1,2,3,4,5,6] Output: 6
# Example 2:
# Input: root = [] Output: 0
# Example 3:
# Input: root = [1] Output: 1
# Constraints:
# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.
#
# 中文:
# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
# 完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
# 示例 1：
# 输入：root = [1,2,3,4,5,6] 输出：6
# 示例 2：
# 输入：root = [] 输出：0
# 示例 3：
# 输入：root = [1] 输出：1
# 提示：
# 树中节点的数目范围是[0, 5 * 104]
# 0 <= Node.val <= 5 * 104
# 题目数据保证输入的树是 完全二叉树
# 进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        hl = 0
        p = root
        while p:
            p = p.left
            hl += 1
        hr = 0
        p = root
        while p:
            p = p.right
            hr += 1
        if hl == hr:
            return 2 ** hl - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
