# -*- coding:utf-8 -*-


# English:
# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
# Example 1:
# Input: root = [3,9,20,null,null,15,7] Output: [[15,7],[9,20],[3]]
# Example 2:
# Input: root = [1] Output: [[1]]
# Example 3:
# Input: root = [] Output: []
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
#
# 中文:
# 给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7] 输出：[[15,7],[9,20],[3]]
# 示例 2：
# 输入：root = [1] 输出：[[1]]
# 示例 3：
# 输入：root = [] 输出：[]
# 提示：
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000


#
# @lc app=leetcode.cn id=107 lang=python
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (58.60%)
# Total Accepted:    12.6K
# Total Submissions: 21.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其自底向上的层次遍历为：
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
#
#
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ret = [[root.val]]
        level = [root]
        while level:
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                ret.append([i.val for i in next_level])
            level = next_level
        return ret[::-1]

if __name__ == "__main__":
    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)
    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7
    s = Solution().levelOrderBottom(n3)
    print(s)

