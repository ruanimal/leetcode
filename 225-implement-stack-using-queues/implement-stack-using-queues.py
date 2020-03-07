# -*- coding:utf-8 -*-


# English:
# Implement the following operations of a stack using queues.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Example:
# MyStack stack = new MyStack(); stack.push(1); stack.push(2); stack.top(); // returns 2 stack.pop(); // returns 2 stack.empty(); // returns false
# Notes:
# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
#
# 中文:
# 使用队列实现栈的下列操作：
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 注意:
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。


#
# @lc app=leetcode.cn id=225 lang=python
#
# [225] 用队列实现栈
#
# https://leetcode-cn.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (54.98%)
# Total Accepted:    8.2K
# Total Submissions: 14.3K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 使用队列实现栈的下列操作：
#
#
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
#
#
# 注意:
#
#
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty
# 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
#
#
#

try:
    from queue import Queue
except ImportError:
    from Queue import Queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_q = Queue()
        self.tmp_q = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack_q.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.stack_q.empty():
            return

        tmp = None
        while not self.stack_q.empty():
            tmp = self.stack_q.get()
            if self.stack_q.empty():
                break
            self.tmp_q.put(tmp)
        self.stack_q, self.tmp_q = self.tmp_q, self.stack_q
        return tmp

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.stack_q.empty():
            return

        t = self.pop()
        self.push(t)
        return t

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.stack_q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.pop())
    print(obj.top())
    print(obj.empty())

