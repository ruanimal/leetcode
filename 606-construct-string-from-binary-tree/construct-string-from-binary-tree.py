# -*- coding:utf-8 -*-


# English:
# You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
# The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
# Example 1:
#
# Input: Binary tree: [1,2,3,4] 1 / \ 2 3 / 4 Output: "1(2(4))(3)"
# Explanation: Originallay it needs to be "1(2(4)())(3()())",
# but you need to omit all the unnecessary empty parenthesis pairs.
# And it will be "1(2(4))(3)".
# Example 2:
#
# Input: Binary tree: [1,2,3,null,4] 1 / \ 2 3 \ 4 Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example,
# except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
#
# 中文:
# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
# 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
# 示例 1:
# 输入: 二叉树: [1,2,3,4] 1 / \ 2 3 / 4 输出: "1(2(4))(3)" 解释: 原本将是“1(2(4)())(3())”， 在你省略所有不必要的空括号对之后， 它将是“1(2(4))(3)”。
# 示例 2:
# 输入: 二叉树: [1,2,3,null,4] 1 / \ 2 3 \ 4 输出: "1(2()(4))(3)" 解释: 和第一个示例相似， 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。


#
# @lc app=leetcode.cn id=606 lang=python
#
# [606] 根据二叉树创建字符串
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        if not t.left and not t.right:
            return '{}'.format(t.val)

        if t.left and t.right:
            return '{}({})({})'.format(t.val,
                self.tree2str(t.left), self.tree2str(t.right))
        if t.left:
            return '{}({})'.format(t.val, self.tree2str(t.left))
        if t.right:
            return '{}()({})'.format(t.val, self.tree2str(t.right))


