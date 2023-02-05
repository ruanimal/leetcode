# -*- coding:utf-8 -*-

# <SUBID:287181528,UPDATE:20230205>
# English:
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.
# Example 1:
# Input: root = [5,3,6,2,4,null,7], key = 3 Output: [5,4,6,2,null,null,7] Explanation: Given key to delete is 3. So we find the node with value 3 and delete it. One valid answer is [5,4,6,2,null,null,7], shown in the above BST. Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
# Example 2:
# Input: root = [5,3,6,2,4,null,7], key = 0 Output: [5,3,6,2,4,null,7] Explanation: The tree does not contain a node with value = 0.
# Example 3:
# Input: root = [], key = 0 Output: []
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105
# Follow up: Could you solve it with time complexity O(height of tree)?
#
# 中文:
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
# 一般来说，删除节点可分为两个步骤：
# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 示例 1:
# 输入：root = [5,3,6,2,4,null,7], key = 3 输出：[5,4,6,2,null,null,7] 解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。 另一个正确答案是 [5,2,6,null,4,null,7]。
# 示例 2:
# 输入: root = [5,3,6,2,4,null,7], key = 0 输出: [5,3,6,2,4,null,7] 解释: 二叉树不包含值为 0 的节点
# 示例 3:
# 输入: root = [], key = 0 输出: []
# 提示:
# 节点数的范围 [0, 104].
# -105 <= Node.val <= 105
# 节点值唯一
# root 是合法的二叉搜索树
# -105 <= key <= 105
# 进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        返回的是删除完对应值的, 新树的根节点
        """

        if root is None:
            return None
        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            min_node = self.get_min(root.right)
            root.right = self.deleteNode(root.right, min_node.val)
            min_node.left = root.left
            min_node.right = root.right
            root = min_node
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def get_min(self, root) -> TreeNode:
        while root.left:
            root = root.left
        return root


