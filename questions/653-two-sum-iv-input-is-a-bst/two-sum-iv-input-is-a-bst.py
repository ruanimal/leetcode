# -*- coding:utf-8 -*-

# <SUBID:319145820,UPDATE:20230205>
# English:
# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9 Output: true
# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28 Output: false
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105
#
# 中文:
# 给定一个二叉搜索树 root 和一个目标结果 k，如果二叉搜索树中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# 示例 1：
# 输入: root = [5,3,6,2,4,null,7], k = 9 输出: true
# 示例 2：
# 输入: root = [5,3,6,2,4,null,7], k = 28 输出: false
# 提示:
# 二叉树的节点个数的范围是  [1, 104].
# -104 <= Node.val <= 104
# 题目数据保证，输入的 root 是一棵 有效 的二叉搜索树
# -105 <= k <= 105


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """遍历二叉树, 转化为twosum问题"""

        def traverse(root):
            if not root:
                return
            nodes_map[root.val] = id(root)
            traverse(root.left)
            traverse(root.right)

        nodes_map = {}
        traverse(root)
        for key, val in nodes_map.items():
            # 防止某个节点被使用两次
            if (k - key) in nodes_map and nodes_map[k - key] != val:
                return True
        return False

