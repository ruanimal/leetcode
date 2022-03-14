# -*- coding:utf-8 -*-


# English:
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
# Example 1:
# Input: root = [4,2,6,1,3] Output: 1
# Example 2:
# Input: root = [1,0,48,null,null,12,49] Output: 1
# Constraints:
# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105
# Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
#
# 中文:
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 差值是一个正数，其数值等于两值之差的绝对值。
# 示例 1：
# 输入：root = [4,2,6,1,3] 输出：1
# 示例 2：
# 输入：root = [1,0,48,null,null,12,49] 输出：1
# 提示：
# 树中节点的数目范围是 [2, 104]
# 0 <= Node.val <= 105
# 注意：本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同


#
# @lc app=leetcode.cn id=530 lang=python
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (51.54%)
# Total Accepted:    3.2K
# Total Submissions: 6.1K
# Testcase Example:  '[1,null,3,2]'
#
# 给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。
#
# 示例 :
#
#
# 输入:
#
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
#
# 输出:
# 1
#
# 解释:
# 最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
#
#
# 注意: 树中至少有2个节点。
#
#
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
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

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(4)

    n1.right = n3
    n3.left = n2
    n3.right = n4
    n3.right = TreeNode(5)
    s = Solution().getMinimumDifference(n1)
    print(s)



