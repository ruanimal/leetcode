# -*- coding:utf-8 -*-


# English:
# Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.
# Do NOT use system's Math.random().
# Example 1:
# Input: 1 Output: [7]
# Example 2:
# Input: 2 Output: [8,4]
# Example 3:
# Input: 3 Output: [8,1,10]
# Note:
# rand7 is predefined.
# Each testcase has one argument: n, the number of times that rand10 is called.
# Follow up:
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?
#
# 中文:
# 已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。
# 不要使用系统的 Math.random() 方法。
# 示例 1:
# 输入: 1 输出: [7]
# 示例 2:
# 输入: 2 输出: [8,4]
# 示例 3:
# 输入: 3 输出: [8,1,10]
# 提示:
# rand7 已定义。
# 传入参数: n 表示 rand10 的调用次数。
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



