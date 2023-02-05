# -*- coding:utf-8 -*-

# <SUBID:318962996,UPDATE:20230205>
# English:
# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
# Example 1:
# Input: c = 5 Output: true Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: c = 3 Output: false
# Constraints:
# 0 <= c <= 231 - 1
#
# 中文:
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
# 示例 1：
# 输入：c = 5 输出：true 解释：1 * 1 + 2 * 2 = 5
# 示例 2：
# 输入：c = 3 输出：false
# 提示：
# 0 <= c <= 231 - 1


#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# https://leetcode-cn.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (29.91%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 19.7K
# Testcase Example:  '5'
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c。
#
# 示例1:
#
#
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
#
#
#
#
# 示例2:
#
#
# 输入: 3
# 输出: False
#
#
#
class Solution(object):
    def judgeSquareSum(self, c: int) -> bool:
        """双指针"""

        import math
        max_val = math.sqrt(c)
        a = 0
        b = int(max_val)
        while a <= b:
            tmp = a ** 2 + b ** 2
            if c == tmp:
                return True
            elif c > tmp:
                a += 1
            else:
                b -= 1
        return False

if __name__ == "__main__":
    s = Solution().judgeSquareSum(4)
    print(s)
    s = Solution().judgeSquareSum(0)
    print(s)
    s = Solution().judgeSquareSum(5)
    print(s)
    s = Solution().judgeSquareSum(6)
    print(s)


