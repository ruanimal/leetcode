# -*- coding:utf-8 -*-


# English:
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
# struct Node { int val; Node *left; Node *right; Node *next; }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Example 1:
# Input: root = [1,2,3,4,5,6,7] Output: [1,#,2,3,#,4,5,6,7,#] Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:
# Input: root = [] Output: []
# Constraints:
# The number of nodes in the tree is in the range [0, 212 - 1].
# -1000 <= Node.val <= 1000
# Follow-up:
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
#
# 中文:
# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
# struct Node { int val; Node *left; Node *right; Node *next; }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 初始状态下，所有 next 指针都被设置为 NULL。
# 示例 1：
# 输入：root = [1,2,3,4,5,6,7] 输出：[1,#,2,3,#,4,5,6,7,#] 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
# 示例 2:
# 输入：root = [] 输出：[]
# 提示：
# 树中节点的数量在
# [0, 212 - 1] 范围内
# -1000 <= node.val <= 1000
# 进阶：
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。



try:
    from comm import *
except ImportError:
    LOCAL_TEST = False

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        que = []
        que.append(root)
        while len(que) > 0:
            p = que[0]
            for i in que[1:]:
                p.next = i
                p = p.next
            next_que = []
            for i in que:
                if i.left:
                    next_que.append(i.left)
                if i.right:
                    next_que.append(i.right)
            que = next_que
        return root


