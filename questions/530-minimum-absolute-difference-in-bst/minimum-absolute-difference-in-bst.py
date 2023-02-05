# -*- coding:utf-8 -*-

# <SUBID:317698759,UPDATE:20230205>
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



class Solution(object):
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.pre_val = None
        self.ans = float('inf')
        self.traverse(root)
        return self.ans

    def traverse(self, root: TreeNode):
        if not root:
            return
        self.traverse(root.left)
        if self.pre_val is not None:
            self.ans = min(self.ans, abs(root.val - self.pre_val))
        self.pre_val = root.val
        self.traverse(root.right)
