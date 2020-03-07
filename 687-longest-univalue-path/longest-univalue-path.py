# -*- coding:utf-8 -*-


# English:
# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
# The length of path between two nodes is represented by the number of edges between them.
# Example 1:
# Input:
# 5 / \ 4 5 / \ \ 1 1 5
# Output: 2
# Example 2:
# Input:
# 1 / \ 4 5 / \ \ 4 4 5
# Output: 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
#
# 中文:
# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
# 注意：两个节点之间的路径长度由它们之间的边数表示。
# 示例 1:
# 输入:
# 5 / \ 4 5 / \ \ 1 1 5
# 输出:
# 2
# 示例 2:
# 输入:
# 1 / \ 4 5 / \ \ 4 4 5
# 输出:
# 2
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。


#
# @lc app=leetcode.cn id=687 lang=python
#
# [687] 最长同值路径
#
# https://leetcode-cn.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (32.93%)
# Total Accepted:    2.9K
# Total Submissions: 8.7K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
#
# 注意：两个节点之间的路径长度由它们之间的边数表示。
#
# 示例 1:
#
# 输入:
#
#
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
#
#
# 输出:
#
#
# 2
#
#
# 示例 2:
#
# 输入:
#
#
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
#
#
# 输出:
#
#
# 2
#
#
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
#
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def ans_length(n):
            if not n:
                return 0
            ans_left = ans_length(n.left)   # 左子箭头最大长度
            ans_right = ans_length(n.right)
            left_part = right_part = 0
            if n.left and n.left.val == n.val:  # 该节点值和左边相同, 路径延伸了1
                left_part = ans_left + 1
            if n.right and n.right.val == n.val:
                right_part = ans_right + 1
            self.ans = max(self.ans, left_part + right_part)  # 往左右两边延伸
            return max(right_part, left_part)  # 改节点单向延展的最大长度为左右半边的大值
        ans_length(root)
        return self.ans

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(4)

    n1.right = n3
    n3.left = n2
    n3.right = n4
    n4.right = TreeNode(5)
    s = Solution().longestUnivaluePath(n1)
    print(s)


