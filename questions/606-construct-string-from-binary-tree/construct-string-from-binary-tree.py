# -*- coding:utf-8 -*-

# <SUBID:19456995,UPDATE:20230205>
# English:
# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
# Example 1:
# Input: root = [1,2,3,4] Output: "1(2(4))(3)" Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
# Example 2:
# Input: root = [1,2,3,null,4] Output: "1(2()(4))(3)" Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -1000 <= Node.val <= 1000
#
# 中文:
# 给你二叉树的根节点 root ，请你采用前序遍历的方式，将二叉树转化为一个由括号和整数组成的字符串，返回构造出的字符串。
# 空节点使用一对空括号对 "()" 表示，转化后需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
# 示例 1：
# 输入：root = [1,2,3,4] 输出："1(2(4))(3)" 解释：初步转化后得到 "1(2(4)())(3()())" ，但省略所有不必要的空括号对后，字符串应该是"1(2(4))(3)" 。
# 示例 2：
# 输入：root = [1,2,3,null,4] 输出："1(2()(4))(3)" 解释：和第一个示例类似，但是无法省略第一个空括号对，否则会破坏输入与输出一一映射的关系。
# 提示：
# 树中节点的数目范围是 [1, 104]
# -1000 <= Node.val <= 1000


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


