# -*- coding:utf-8 -*-

# <SUBID:317808616,UPDATE:20230205>
# English:
# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
# Example 1:
# Input: root = [1,null,3,2,4,null,5,6] Output: 3
# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] Output: 5
# Constraints:
# The total number of nodes is in the range [0, 104].
# The depth of the n-ary tree is less than or equal to 1000.
#
# 中文:
# 给定一个 N 叉树，找到其最大深度。
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
# N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。
# 示例 1：
# 输入：root = [1,null,3,2,4,null,5,6] 输出：3
# 示例 2：
# 输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] 输出：5
# 提示：
# 树的深度不会超过 1000 。
# 树的节点数目位于 [0, 104] 之间。



class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: None) -> int:
        """递归法"""

        if not root:
            return 0

        max_depth = 1
        for i in root.children:
            max_depth = max(max_depth, 1 + self.maxDepth(i))
        return max_depth

