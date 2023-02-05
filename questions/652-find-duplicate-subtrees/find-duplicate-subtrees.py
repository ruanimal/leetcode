# -*- coding:utf-8 -*-

# <SUBID:283782486,UPDATE:20230205>
# English:
# Given the root of a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with the same node values.
# Example 1:
# Input: root = [1,2,3,4,null,2,4,null,null,4] Output: [[2,4],[4]]
# Example 2:
# Input: root = [2,1,1] Output: [[1]]
# Example 3:
# Input: root = [2,2,2,3,null,3,null] Output: [[2,3],[3]]
# Constraints:
# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200
#
# 中文:
# 给你一棵二叉树的根节点 root ，返回所有 重复的子树 。
# 对于同一类的重复子树，你只需要返回其中任意 一棵 的根结点即可。
# 如果两棵树具有 相同的结构 和 相同的结点值 ，则认为二者是 重复 的。
# 示例 1：
# 输入：root = [1,2,3,4,null,2,4,null,null,4] 输出：[[2,4],[4]]
# 示例 2：
# 输入：root = [2,1,1] 输出：[[1]]
# 示例 3：
# 输入：root = [2,2,2,3,null,3,null] 输出：[[2,3],[3]]
# 提示：
# 树中的结点数在 [1, 5000] 范围内。
# -200 <= Node.val <= 200


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
try:
    from comm import *
except ImportError:
    LOCAL_TEST = False

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return

        self.memo = {}
        self.res = []
        self.postorder(root)
        return self.res

    def postorder(self, root) -> List:
        if not root:
            return '#'
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        ident = '{},{},{}'.format(left, right, root.val)
        count = self.memo.get(ident, 0)
        if count == 1:
            self.res.append(root)
        self.memo[ident] = count + 1
        return ident


