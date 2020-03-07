# -*- coding:utf-8 -*-


# English:
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Example 1:
# Input: 121 Output: true
# Example 2:
# Input: -121 Output: false Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
# Input: 10 Output: false Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
# Coud you solve it without converting the integer to a string?
#
# 中文:
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 示例 1:
# 输入: 121 输出: true
# 示例 2:
# 输入: -121 输出: false 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
# 输入: 10 输出: false 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 进阶:
# 你能不将整数转为字符串来解决这个问题吗？


#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (56.05%)
# Total Accepted:    70.1K
# Total Submissions: 125K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
#
#
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？
#
#

class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        # import math
        if x < 0:
            return False
        # n = int(math.log10(x)) + 1  # 位数
        n = len(str(x))
        # while x != 0:
        #     x, s = divmod(x, 10)  # 商, 余数,
        #     tmp.append(s)
        for i in range(n//2):
            i += 1
            x, tail = divmod(x, 10)
            base = 10 ** (n-2*i)
            head = x // base
            x = x % base
            if head != tail:
                return False
        return True

if __name__ == '__main__':
    # import ipdb; ipdb.set_trace()
    print(Solution().isPalindrome(12221))

