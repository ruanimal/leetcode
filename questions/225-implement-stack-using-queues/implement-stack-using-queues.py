# -*- coding:utf-8 -*-


# English:
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
# Implement the MyStack class:
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
# Example 1:
# Input ["MyStack", "push", "push", "top", "pop", "empty"] [[], [1], [2], [], [], []] Output [null, null, null, 2, 2, false] Explanation MyStack myStack = new MyStack(); myStack.push(1); myStack.push(2); myStack.top(); // return 2 myStack.pop(); // return 2 myStack.empty(); // return False
# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
# Follow-up: Can you implement the stack using only one queue?
#
# 中文:
# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
# 实现 MyStack 类：
# void push(int x) 将元素 x 压入栈顶。
# int pop() 移除并返回栈顶元素。
# int top() 返回栈顶元素。
# boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
# 注意：
# 你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
# 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 示例：
# 输入： ["MyStack", "push", "push", "top", "pop", "empty"] [[], [1], [2], [], [], []] 输出： [null, null, null, 2, 2, false] 解释： MyStack myStack = new MyStack(); myStack.push(1); myStack.push(2); myStack.top(); // 返回 2 myStack.pop(); // 返回 2 myStack.empty(); // 返回 False
# 提示：
# 1 <= x <= 9
# 最多调用100 次 push、pop、top 和 empty
# 每次调用 pop 和 top 都保证栈不为空
# 进阶：你能否仅用一个队列来实现栈。


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

