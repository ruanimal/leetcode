# -*- coding:utf-8 -*-


# English:
# Implement the following operations of a queue using stacks.
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Example:
# MyQueue queue = new MyQueue(); queue.push(1); queue.push(2); queue.peek(); // returns 1 queue.pop(); // returns 1 queue.empty(); // returns false
# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
#
# 中文:
# 使用栈实现队列的下列操作：
# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。
# 示例:
# MyQueue queue = new MyQueue(); queue.push(1); queue.push(2); queue.peek(); // 返回 1 queue.pop(); // 返回 1 queue.empty(); // 返回 false
# 说明:
# 你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。


#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#
# https://leetcode-cn.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (57.27%)
# Total Accepted:    8.8K
# Total Submissions: 14.9K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 使用栈实现队列的下列操作：
#
#
# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。
#
#
# 示例:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false
#
# 说明:
#
#
# 你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty
# 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
#
#
#
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_stack = []
        self.tmp_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.data_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.data_stack:
            return

        while self.data_stack:
            self.tmp_stack.append(self.data_stack.pop())
        data = self.tmp_stack.pop()
        while self.tmp_stack:
            self.data_stack.append(self.tmp_stack.pop())
        return data

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.data_stack:
            return self.data_stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.data_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.pop()
    obj.peek()
    print(obj.data_stack)
    print(obj.tmp_stack)


