# -*- coding:utf-8 -*-

# <SUBID:308518285,UPDATE:20230205>
# English:
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Example 1:
# Input: x = 2.00000, n = 10 Output: 1024.00000
# Example 2:
# Input: x = 2.10000, n = 3 Output: 9.26100
# Example 3:
# Input: x = 2.00000, n = -2 Output: 0.25000 Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Constraints:
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# -104 <= xn <= 104
#
# 中文:
# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。
# 示例 1：
# 输入：x = 2.00000, n = 10 输出：1024.00000
# 示例 2：
# 输入：x = 2.10000, n = 3 输出：9.26100
# 示例 3：
# 输入：x = 2.00000, n = -2 输出：0.25000 解释：2-2 = 1/22 = 1/4 = 0.25
# 提示：
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n 是一个整数
# -104 <= xn <= 104


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        n 有两种情况 奇数 或者 偶数, 注意保存结果防止重复调用
        奇数 myPow(x, n//2) * myPow(x, n//2) * x
        偶数 myPow(x, n//2) * myPow(x, n//2)
        """

        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        if n == 1:
            return x
        n, flag = divmod(n, 2)
        tmp = self.myPow(x, n)
        return tmp * tmp * x if flag else tmp * tmp

