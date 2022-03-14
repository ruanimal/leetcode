# -*- coding:utf-8 -*-


# English:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Example 1:
# Input ["MinStack","push","push","push","getMin","pop","top","getMin"] [[],[-2],[0],[-3],[],[],[],[]] Output [null,null,null,null,-3,null,0,-2] Explanation MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); // return -3 minStack.pop(); minStack.top(); // return 0 minStack.getMin(); // return -2
# Constraints:
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.
#
# 中文:
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 实现 MinStack 类:
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
# 示例 1:
# 输入： ["MinStack","push","push","push","getMin","pop","top","getMin"] [[],[-2],[0],[-3],[],[],[],[]] 输出： [null,null,null,null,-3,null,0,-2] 解释： MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); --> 返回 -3. minStack.pop(); minStack.top(); --> 返回 0. minStack.getMin(); --> 返回 -2.
# 提示：
# -231 <= val <= 231 - 1
# pop、top 和 getMin 操作总是在 非空栈 上调用
# push, pop, top, and getMin最多被调用 3 * 104 次


#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (47.24%)
# Total Accepted:    21.2K
# Total Submissions: 44K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
#
#
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return

        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return

        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return

        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(3)
    obj.push(2)
    print(obj.getMin())
    print(obj.pop())
    print(obj.getMin())


