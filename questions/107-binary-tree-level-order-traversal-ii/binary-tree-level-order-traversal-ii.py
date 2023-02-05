# -*- coding:utf-8 -*-

# <SUBID:308719450,UPDATE:20230205>
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



class Solution(object):
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        层次遍历然后反转
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

