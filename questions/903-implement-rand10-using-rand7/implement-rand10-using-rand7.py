# -*- coding:utf-8 -*-


# English:
# Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.
# Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().
# Example 1:
# Input: n = 1 Output: [2]
# Example 2:
# Input: n = 2 Output: [2,8]
# Example 3:
# Input: n = 3 Output: [3,8,10]
# Constraints:
# 1 <= n <= 105
# Follow up:
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?
#
# 中文:
# 给定方法 rand7 可生成 [1,7] 范围内的均匀随机整数，试写一个方法 rand10 生成 [1,10] 范围内的均匀随机整数。
# 你只能调用 rand7() 且不能调用其他方法。请不要使用系统的 Math.random() 方法。
# 每个测试用例将有一个内部参数 n，即你实现的函数 rand10() 在测试时将被调用的次数。请注意，这不是传递给 rand10() 的参数。
# 示例 1:
# 输入: 1 输出: [2]
# 示例 2:
# 输入: 2 输出: [2,8]
# 示例 3:
# 输入: 3 输出: [3,8,10]
# 提示:
# 1 <= n <= 105
# 进阶:
# rand7()调用次数的 期望值 是多少 ?
# 你能否尽量少调用 rand7() ?


#
# @lc app=leetcode.cn id=470 lang=python
#
# [470] Implement Rand10() Using Rand7()
#
# https://leetcode-cn.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (39.21%)
# Total Accepted:    1.2K
# Total Submissions: 3K
# Testcase Example:  '1'
#
# 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
#
# 不要使用系统的 Math.random() 方法。
#
#
#
#
#
#
# 示例 1:
#
#
# 输入: 1
# 输出: [7]
#
#
# 示例 2:
#
#
# 输入: 2
# 输出: [8,4]
#
#
# 示例 3:
#
#
# 输入: 3
# 输出: [8,1,10]
#
#
#
#
# 提示:
#
#
# rand7 已定义。
# 传入参数: n 表示 rand10 的调用次数。
#
#
#
#
# 进阶:
#
#
# rand7()调用次数的 期望值 是多少 ?
# 你能否尽量少调用 rand7() ?
#
#
#
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        枚举如下：
            a	1	2	3	4	5	6	7
        b
        1		2	3	4	5	6	7	8
        2		3	4	5	6	7	8	9
        3		4	5	6	7	8	9	0
        4		5	6	7	8	9	0	1
        5		6	7	8	9	0	1	2
        6		7	8	9	0	1	2	3
        7		8	9	0	1	2	3	4
        去掉右上角的
        6	7	8
        7	8	9
        8	9	0      后

        每个数字的出现次数为4次，0-9的概率相同

        所以程序思路就很明了,当结果扫到右上角的时候进行递归调用，直到输出其他结果
        平均调用2.3次rand7()
        """
        a=rand7()
        b=rand7()
        if(a>4 and b<4):
            return self.rand10()
        else:
            return (a+b)%10+1



