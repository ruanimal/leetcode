# -*- coding:utf-8 -*-

# <SUBID:21033175,UPDATE:20220325>
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
# @lc app=leetcode.cn id=633 lang=python
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
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # # 暴力二分查找, 超时
        # import math
        # def func(base):
        #     f = lambda x: x**2 + base
        #     i = -1
        #     j = int(math.sqrt(c)) + 1
        #     while i < j-1:
        #         # print(i, j)
        #         mid = (i+j)//2
        #         if f(mid) > c:
        #             j = mid
        #         elif f(mid) < c:
        #             i = mid
        #         else:
        #             return True
        #     return False

        # for i in range(int(math.sqrt(c))+1):
        #     if func(i**2):
        #         return True
        # return False
        # long int a = sqrt(c);
        # if(a == sqrt(c)) return 1;
        # long int b = 1;
        # long int d = a;
        # while((b + d > a) && (d - b < a))
        # {
        #     if(c == b*b + d*d) return 1;
        #     else if(c > b*b + d*d) b++;
        #     else d--;
        # }
        # return 0;
        import math
        a = math.sqrt(c)
        if a == int(a):
            return True
        a = int(a)
        b = 1
        d = a
        while (b + d > a) and (d - b < a):
            if c == b ** 2 + d ** 2:
                return True
            elif c > b ** 2 + d ** 2:
                b += 1
            else:
                d -= 1
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


