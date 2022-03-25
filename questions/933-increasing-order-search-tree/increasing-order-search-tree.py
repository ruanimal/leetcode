# -*- coding:utf-8 -*-

# <SUBID:18590935,UPDATE:20220325>
# English:
# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
# Example 1:
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9] Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# Example 2:
# Input: root = [5,1,7] Output: [1,null,5,null,7]
# Constraints:
# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000
#
# 中文:
# 给你一棵二叉搜索树的
# root ，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
# 示例 1：
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9] 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 示例 2：
# 输入：root = [5,1,7] 输出：[1,null,5,null,7]
# 提示：
# 树中节点数的取值范围是 [1, 100]
# 0 <= Node.val <= 1000


#
# @lc app=leetcode.cn id=897 lang=python
#
# [897] 递增顺序查找树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root, tail=None):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 纯递归解法, 比较难理解
        # if not root:
        #     return tail
        # r = self.increasingBST(root.left, root)
        # root.left = None
        # root.right = self.increasingBST(root.right, tail)
        # return r

        def mid_dfs(node, ret=None):
            if ret is None:
                ret = []
            if not node:
                return
            mid_dfs(node.left, ret)
            node.left = None
            ret.append(node)
            mid_dfs(node.right, ret)
            return ret
        ret = mid_dfs(root)
        ret[-1].right = None   # 去除旧的右节点
        ans = ret[0]
        for i in range(len(ret)-1):
            ret[i].right = ret[i+1]
        return ans


