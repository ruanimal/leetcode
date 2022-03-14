# -*- coding:utf-8 -*-


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


#
# @lc app=leetcode.cn id=559 lang=python
#
# [559] Maximum Depth of N-ary Tree
#
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (64.19%)
# Total Accepted:    5.5K
# Total Submissions: 8.5K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# 给定一个 N 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 我们应返回其最大深度，3。
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。
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

    def __repr__(self):
        return 'Node(%r, %r)' % (self.val, self.children)

class Solution(object):
    def maxDepth1(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def dfs(node):
            if not node.children:
                max_depth[0] = max(max_depth[0], len(tmp))
                return

            for i in node.children:
                tmp.append(i)
                dfs(i)
                tmp.pop()

        if not root:
            return 0

        max_depth = [0]
        tmp = [root]
        dfs(root)
        return max_depth[0]

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        print('=')
        if not root:
            return 0

        max_depth = 1
        for i in root.children:
            max_depth = max(max_depth, 1 + self.maxDepth(i))
        return max_depth

if __name__ == "__main__":
    n1 = Node(1, [Node(2, []), Node(3, [])])
    root = Node(0, [n1])
    s = Solution().maxDepth(root)
    print(s)
    s = Solution().maxDepth1(root)
    print(s)


