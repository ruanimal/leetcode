# -*- coding:utf-8 -*-

# <SUBID:287150117,UPDATE:20230205>
# English:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
# Input: root = [2,1,3] Output: true
# Example 2:
# Input: root = [5,1,4,null,null,3,6] Output: false Explanation: The root node's value is 5 but its right child's value is 4.
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1
#
# 中文:
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 有效 二叉搜索树定义如下：
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1：
# 输入：root = [2,1,3] 输出：true
# 示例 2：
# 输入：root = [5,1,4,null,null,3,6] 输出：false 解释：根节点的值是 5 ，但是右子节点的值是 4 。
# 提示：
# 树中节点数目范围在[1, 104] 内
# -231 <= Node.val <= 231 - 1



class Solution(object):
    def isValidBST(self, root, min_val=float('-inf'), max_val=float('+inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.val <= min_val:
            return False
        if root.val >= max_val:
            return False
        return (self.isValidBST(root.left, min_val, min(root.val, max_val))
                and self.isValidBST(root.right, max(root.val, min_val), max_val))

