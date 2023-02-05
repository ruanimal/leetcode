# -*- coding:utf-8 -*-

# <SUBID:287233490,UPDATE:20230205>
# English:
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 Output: 3 Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 Output: 5 Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:
# Input: root = [1,2], p = 1, q = 2 Output: 1
# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
#
# 中文:
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 示例 1：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 输出：3 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
# 示例 2：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 输出：5 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
# 示例 3：
# 输入：root = [1,2], p = 1, q = 2 输出：1
# 提示：
# 树中节点数目在范围 [2, 105] 内。
# -109 <= Node.val <= 109
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_A:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        求出两个点的路径, 再比较路径从什么时候开始不同
        """
        if root is None:
            return

        self.tmp = []
        self.helper(root, p, [])
        self.helper(root, q, [])
        path_p, path_q = self.tmp
        for i in range(min(len(path_p), len(path_q))-1, -1, -1):
            if path_p[i].val == path_q[i].val:
                return path_p[i]
        return root

    def helper(self, root: TreeNode, target: TreeNode, path: List[TreeNode]) -> None:
        if root is None:
            return
        path.append(root)
        if root.val == target.val:
            self.tmp.append(path[:])
            return
        self.helper(root.left, target, path)
        self.helper(root.right, target, path)
        path.pop()


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        递归版本

        返回值含义: 在子树中是否存在该节点, 并返回该节点
        """
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left is None and right is None:
            return None
        return right if left is None else left

