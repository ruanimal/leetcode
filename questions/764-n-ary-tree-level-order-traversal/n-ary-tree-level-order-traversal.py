# -*- coding:utf-8 -*-

# <SUBID:315017524,UPDATE:20230205>
# English:
# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
# Example 1:
# Input: root = [1,null,3,2,4,null,5,6] Output: [[1],[3,2,4],[5,6]]
# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
# Constraints:
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 104]
#
# 中文:
# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
# 树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
# 示例 1：
# 输入：root = [1,null,3,2,4,null,5,6] 输出：[[1],[3,2,4],[5,6]]
# 示例 2：
# 输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] 输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
# 提示：
# 树的高度不会超过 1000
# 树的节点总数在 [0, 10^4] 之间



class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []

        ret = [[root.val]]
        level = [root]
        while level:
            next_level = []
            for node in level:
                next_level.extend(node.children)
            if next_level:
                ret.append([i.val for i in next_level])
            level = next_level
        return ret

