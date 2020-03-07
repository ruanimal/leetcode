# -*- coding:utf-8 -*-


# English:
# You are standing at position 0 on an infinite number line. There is a goal at position target.
# On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.
# Return the minimum number of steps required to reach the destination.
# Example 1:
#
# Input: target = 3 Output: 2 Explanation: On the first move we step from 0 to 1. On the second step we step from 1 to 3.
# Example 2:
#
# Input: target = 2 Output: 3 Explanation: On the first move we step from 0 to 1. On the second move we step from 1 to -1. On the third move we step from -1 to 2.
# Note:
#
# target will be a non-zero integer in the range [-10^9, 10^9].
#
# 中文:
# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。
# 每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。
# 返回到达终点需要的最小移动次数。
# 示例 1:
# 输入: target = 3 输出: 2 解释: 第一次移动，从 0 到 1 。 第二次移动，从 1 到 3 。
# 示例 2:
# 输入: target = 2 输出: 3 解释: 第一次移动，从 0 到 1 。 第二次移动，从 1 到 -1 。 第三次移动，从 -1 到 2 。
# 注意:
# target是在[-10^9, 10^9]范围中的非零整数。


#
# @lc app=leetcode.cn id=754 lang=python
#
# [754] 到达终点数字
#
# https://leetcode-cn.com/problems/reach-a-number/description/
#
# algorithms
# Easy (35.80%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 4.8K
# Testcase Example:  '1'
#
# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。
#
# 每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。
#
# 返回到达终点需要的最小移动次数。
#
# 示例 1:
#
#
# 输入: target = 3
# 输出: 2
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 3 。
#
#
# 示例 2:
#
#
# 输入: target = 2
# 输出: 3
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 -1 。
# 第三次移动，从 -1 到 2 。
#
#
# 注意:
#
#
# target是在[-10^9, 10^9]范围中的非零整数。
#
#
#

'''给你一个数，第n次可以向左走，也可以向右走，问你最少多少次可以走到目的地

一开始我考虑的是广度优先遍历解决，但是这样的话由于target太大，内存超了，于是只好考虑其他的方法，思考过后我发现这题用数学的方法解决其实很简单，首先，要到达目的地一定会有向左和向右，我们假设一定有一个最好的方案，
a1,a2,a3…an,假如a1到an都是正数，那么它一定是最好的方案，
假如存在负数，那么可以看成把a1,a2…an里面的若干个数变成负数，然后到达target，

可以证明，当a1+a2..an-target为偶数的时候，只需要把a1,a2,…an里面的一个数变成负数就能到达目的地，这就是最好的方案

当a1+a2..an-target为奇数的时候，有两种情况，
    当n为偶数的时候，n+1为奇数，可以证明，当把a1,a2..an里面一个数变成负数之后，只要在加一个数就能到达target，也就是a1+a2…an+an+1一定可以到达target,
    当n为奇数的时候，可以证明当把a1,a2..an里面一个数变成负数之后只要在加两个个数就能到达target，也就是a1+a2…an+an+1+an+2,所以有以下算法
'''

class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        return k if (target % 2 == 0) else (k + 1 + k%2)


