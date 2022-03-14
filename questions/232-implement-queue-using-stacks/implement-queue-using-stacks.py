# -*- coding:utf-8 -*-


# English:
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
# Example 1:
# Input ["MyQueue", "push", "push", "peek", "pop", "empty"] [[], [1], [2], [], [], []] Output [null, null, null, 1, 1, false] Explanation MyQueue myQueue = new MyQueue(); myQueue.push(1); // queue is: [1] myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue) myQueue.peek(); // return 1 myQueue.pop(); // return 1, queue is [2] myQueue.empty(); // return false
# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.
# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
#
# 中文:
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
# 实现 MyQueue 类：
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
# 说明：
# 你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 示例 1：
# 输入： ["MyQueue", "push", "push", "peek", "pop", "empty"] [[], [1], [2], [], [], []] 输出： [null, null, null, 1, 1, false] 解释： MyQueue myQueue = new MyQueue(); myQueue.push(1); // queue is: [1] myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue) myQueue.peek(); // return 1 myQueue.pop(); // return 1, queue is [2] myQueue.empty(); // return false
# 提示：
# 1 <= x <= 9
# 最多调用 100 次 push、pop、peek 和 empty
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
# 进阶：
# 你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。


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


