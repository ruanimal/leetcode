# -*- coding:utf-8 -*-

# <SUBID:287195670,UPDATE:20230205>
# English:
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
# Example 1:
# Input: root = [4,2,7,1,3], val = 5 Output: [4,2,7,1,3,5] Explanation: Another accepted tree is:
# Example 2:
# Input: root = [40,20,60,10,30,50,70], val = 25 Output: [40,20,60,10,30,50,70,null,null,25]
# Example 3:
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5 Output: [4,2,7,1,3,5]
# Constraints:
# The number of nodes in the tree will be in the range [0, 104].
# -108 <= Node.val <= 108
# All the values Node.val are unique.
# -108 <= val <= 108
# It's guaranteed that val does not exist in the original BST.
#
# 中文:
# 给定二叉搜索树（BST）的根节点
# root 和要插入树中的值
# value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。
# 示例 1：
# 输入：root = [4,2,7,1,3], val = 5 输出：[4,2,7,1,3,5] 解释：另一个满足题目要求可以通过的树是：
# 示例 2：
# 输入：root = [40,20,60,10,30,50,70], val = 25 输出：[40,20,60,10,30,50,70,null,null,25]
# 示例 3：
# 输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5 输出：[4,2,7,1,3,5]
# 提示：
# 树中的节点数将在
# [0, 104]的范围内。
# -108 <= Node.val <= 108
# 所有值
# Node.val 是 独一无二 的。
# -108 <= val <= 108
# 保证 val 在原始BST中不存在。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_A:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        递归写法
        """

        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        pre_root = origin = root
        while root:
            pre_root = root
            if val < root.val:
                root = root.left
            else:
                root = root.right
        if val < pre_root.val:
            pre_root.left = TreeNode(val)
        else:
            pre_root.right = TreeNode(val)
        return origin
