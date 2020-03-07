# -*- coding:utf-8 -*-


# English:
# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
# Example 1:
# Input: root = [1,null,3,2,4,null,5,6] Output: [[1],[3,2,4],[5,6]]
# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
# Constraints:
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]
#
# 中文:
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
# 例如，给定一个 3叉树 :
# 返回其层序遍历:
# [ [1], [3,2,4], [5,6] ]
# 说明:
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。


#
# @lc app=leetcode.cn id=429 lang=python
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Easy (58.66%)
# Total Accepted:    4.3K
# Total Submissions: 7.3K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其层序遍历:
#
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
#
#
#
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。
#
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        from collections import deque

        if not root:
            return []

        ret = []
        que = deque()
        que.append(root)
        while que:
            level_size = len(que)
            level = []
            for i in range(level_size):
                t = que.popleft()
                que.extend(t.children)
                level.append(t.val)
            ret.append(level)
        return ret

if __name__ == "__main__":
    n1 = Node(1, [Node(2, []), Node(3, [Node(4, [])])])
    root = Node(0, [n1])
    s = Solution().levelOrder(root)
    print(s)




