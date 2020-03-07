# -*- coding:utf-8 -*-


# English:
# You are given a binary tree in which each node contains an integer value.
# Find the number of paths that sum to a given value.
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
# Example:
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8 10 / \ 5 -3 / \ \ 3 2 11 / \ \ 3 -2 1 Return 3. The paths that sum to 8 are: 1. 5 -> 3 2. 5 -> 2 -> 1 3. -3 -> 11
#
# 中文:
# 给定一个二叉树，它的每个结点都存放着一个整数值。
# 找出路径和等于给定数值的路径总数。
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
# 示例：
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8 10 / \ 5 -3 / \ \ 3 2 11 / \ \ 3 -2 1 返回 3。和等于 8 的路径有: 1. 5 -> 3 2. 5 -> 2 -> 1 3. -3 -> 11


#
# @lc app=leetcode.cn id=437 lang=python
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (47.76%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 11.1K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
# 示例：
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
#
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# def print_tree(root):
#     level = [root]
#     ans = []
#     while level:
#         ans.append([str(i.val) if i.val is not None else 'n'  for i in level])
#         next_level = []
#         for node in level:
#             if node.left:
#                 next_level.append(node.left)
#             if node.right:
#                 next_level.append(node.right)
#         level = next_level

#     strings = []
#     item_width = 2
#     width = 2 ** len(ans) * 2 * item_width
#     pading = ' ' * item_width
#     for level in range(len(ans)-1, -1, -1):
#         i = ['{:^2}'.format(xx) for xx in ans[level]]
#         partern = '{:^%s}' % (width)
#         raw_line = pading.join(i)
#         if level == (len(ans)-1):
#             raw_line += ((2 ** (level+1)-1) * item_width - len(raw_line)) * ' '
#         # print(repr(raw_line))
#         line = partern.format(raw_line)
#         strings.append(line)
#         pading = ' ' * ((len(pading) + item_width) * 2 - item_width)
#     for i in strings[::-1]:
#         print(i)


# # 不知道为啥, 有个测试用例线上不能通过, 应该是二叉树的结构问题
# # [1,null,2,null,3,null,4,null,5]\n3
# class Solution(object):
#     def pathSum(self, root, sum):
#         """
#         :type root: TreeNode
#         :type sum: int
#         :rtype: int
#         """
#         if not root:
#             return 0
#         print_tree(root)
#         return self.helper(root, sum) + self.helper(root.right, sum) + self.helper(root.left, sum)

#     def helper(self, root, sum):
#         if not root:
#             return 0

#         ans = 0
#         if root.val == sum:
#             ans += 1
#         ans += self.helper(root.right, sum-root.val)
#         ans += self.helper(root.left, sum-root.val)
#         return ans

class Solution(object):
    def pathSum(self, root, sum):
        """抄的答案, 应该是用到了动态规划思想"""

        from collections import defaultdict
        lookup = defaultdict(int)
        lookup[0] = 1
        self.res = 0

        def helper(root,curSum):
            if not root:
                return
            curSum += root.val
            self.res += lookup[curSum - sum]
            lookup[curSum] += 1
            helper(root.left,curSum)
            helper(root.right,curSum)
            lookup[curSum] -= 1
        helper(root,0)
        return self.res

if __name__ == "__main__":
    pass
    # null = None
    # from algorithm.binary_tree_travel import build, print_tree
    # tree = build([1,null,2,null,3,null,4,null,5])
    # print_tree(tree)
    # s = Solution().pathSum(tree, 3)
    # print(s)

