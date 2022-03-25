# -*- coding:utf-8 -*-

# <SUBID:16405986,UPDATE:20220325>
# English:
# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3 Output: false
# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4 Output: true
# Example 3:
# Input: root = [1,2,3,null,4], x = 2, y = 3 Output: false
# Constraints:
# The number of nodes in the tree is in the range [2, 100].
# 1 <= Node.val <= 100
# Each node has a unique value.
# x != y
# x and y are exist in the tree.
#
# 中文:
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。
# 示例 1：
#
# 输入：root = [1,2,3,4], x = 4, y = 3 输出：false
# 示例 2：
#
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4 输出：true
# 示例 3：
# 输入：root = [1,2,3,null,4], x = 2, y = 3 输出：false
# 提示：
# 二叉树的节点数介于 2 到 100 之间。
# 每个节点的值都是唯一的、范围为 1 到 100 的整数。


#
# @lc app=leetcode.cn id=993 lang=python
#
# [993] 最高的广告牌
#
# https://leetcode-cn.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (44.32%)
# Total Accepted:    996
# Total Submissions: 2.2K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
#
# 如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
#
# 我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
#
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
#
#
# 示例 2：
#
#
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
#
#
# 示例 3：
#
#
#
# 输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false
#
#
#
# 提示：
#
#
# 二叉树的节点数介于 2 到 100 之间。
# 每个节点的值都是唯一的、范围为 1 到 100 的整数。
#
#
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
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False

        level = [root]
        parent_map = {root.val:None}
        while level:
            next_level = []
            for node in level:
                if node.left:
                    parent_map[node.left.val] = node.val
                    next_level.append(node.left)
                if node.right:
                    parent_map[node.right.val] = node.val
                    next_level.append(node.right)
            if next_level:
                t = set([i.val for i in next_level])
                if x in t and y in t:
                    if parent_map[x] == parent_map[y]:
                        return False
                    else:
                        return True
                elif x not in t and y not in t:
                    pass
                else:
                    return False
            level = next_level
        return False

