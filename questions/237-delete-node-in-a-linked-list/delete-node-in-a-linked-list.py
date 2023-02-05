# -*- coding:utf-8 -*-

# <SUBID:313348682,UPDATE:20230205>
# English:
# There is a singly-linked list head and we want to delete a node node in it.
# You are given the node to be deleted node. You will not be given access to the first node of head.
# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.
# Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:
# The value of the given node should not exist in the linked list.
# The number of nodes in the linked list should decrease by one.
# All the values before node should be in the same order.
# All the values after node should be in the same order.
# Custom testing:
# For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
# We will build the linked list and pass the node to your function.
# The output will be the entire list after calling your function.
# Example 1:
# Input: head = [4,5,1,9], node = 5 Output: [4,1,9] Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
# Example 2:
# Input: head = [4,5,1,9], node = 1 Output: [4,5,9] Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
# Constraints:
# The number of the nodes in the given list is in the range [2, 1000].
# -1000 <= Node.val <= 1000
# The value of each node in the list is unique.
# The node to be deleted is in the list and is not a tail node.
#
# 中文:
# 有一个单链表的 head，我们想删除它其中的一个节点 node。
# 给你一个需要删除的节点 node 。你将 无法访问 第一个节点  head。
# 链表的所有值都是 唯一的，并且保证给定的节点 node 不是链表中的最后一个节点。
# 删除给定的节点。注意，删除节点并不是指从内存中删除它。这里的意思是：
# 给定节点的值不应该存在于链表中。
# 链表中的节点数应该减少 1。
# node 前面的所有值顺序相同。
# node 后面的所有值顺序相同。
# 自定义测试：
# 对于输入，你应该提供整个链表 head 和要给出的节点 node。node 不应该是链表的最后一个节点，而应该是链表中的一个实际节点。
# 我们将构建链表，并将节点传递给你的函数。
# 输出将是调用你函数后的整个链表。
# 示例 1：
# 输入：head = [4,5,1,9], node = 5 输出：[4,1,9] 解释：指定链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9
# 示例 2：
# 输入：head = [4,5,1,9], node = 1 输出：[4,5,9] 解释：指定链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9
# 提示：
# 链表中节点的数目范围是 [2, 1000]
# -1000 <= Node.val <= 1000
# 链表中每个节点的值都是 唯一 的
# 需要删除的节点 node 是 链表中的节点 ，且 不是末尾节点



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node: ListNode):
        """
        删除当前节点
        """
        if not node:
            return
        node.val = node.next.val
        node.next = node.next.next

