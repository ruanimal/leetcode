# -*- coding:utf-8 -*-


# English:
# Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.
# Example 1: Input: [5,3,6,2,4,null,8,1,null,null,null,7,9] 5 / \ 3 6 / \ \ 2 4 8  / / \ 1 7 9 Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9] 1   \   2   \   3   \   4   \   5   \   6   \   7   \   8   \ 9
# Note:
# The number of nodes in the given tree will be between 1 and 100.
# Each node will have a unique integer value from 0 to 1000.
#
# 中文:
# 给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。
# 示例 ：
# 输入：[5,3,6,2,4,null,8,1,null,null,null,7,9] 5 / \ 3 6 / \ \ 2 4 8  / / \ 1 7 9 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9] 1   \   2   \   3   \   4   \   5   \   6   \   7   \   8   \ 9
# 提示：
# 给定树中的结点数介于 1 和 100 之间。
# 每个结点都有一个从 0 到 1000 范围内的唯一整数值。


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


