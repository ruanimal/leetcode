# -*- coding:utf-8 -*-

# <SUBID:20837406,UPDATE:20220325>
# English:
# You are given a binary array nums (0-indexed).
# We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).
# For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
# Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
# Example 1:
# Input: nums = [0,1,1] Output: [true,false,false] Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10. Only the first number is divisible by 5, so answer[0] is true.
# Example 2:
# Input: nums = [1,1,1] Output: [false,false,false]
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
#
# 中文:
# 给定一个二进制数组 nums ( 索引从0开始 )。
# 我们将xi 定义为其二进制表示形式为子数组 nums[0..i] (从最高有效位到最低有效位)。
# 例如，如果 nums =[1,0,1] ，那么 x0 = 1, x1 = 2, 和 x2 = 5。
# 返回布尔值列表 answer，只有当 xi 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。
# 示例 1：
# 输入：nums = [0,1,1] 输出：[true,false,false] 解释： 输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为 true 。
# 示例 2：
# 输入：nums = [1,1,1] 输出：[false,false,false]
# 提示：
# 1 <= nums.length <= 105
# nums[i] 仅为 0 或 1


#
# @lc app=leetcode.cn id=1018 lang=python
#
# [1018] 可被 5 整除的二进制前缀
#
# https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/description/
#
# algorithms
# Easy (34.85%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 6.5K
# Testcase Example:  '[0,1,1]'
#
# 给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i
# 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。
#
# 返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。
#
#
#
# 示例 1：
#
# 输入：[0,1,1]
# 输出：[true,false,false]
# 解释：
# 输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
#
#
# 示例 2：
#
# 输入：[1,1,1]
# 输出：[false,false,false]
#
#
# 示例 3：
#
# 输入：[0,1,1,1,1,1]
# 输出：[true,false,false,false,true,false]
#
#
# 示例 4：
#
# 输入：[1,1,1,0,1]
# 输出：[false,false,false,false,false]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 30000
# A[i] 为 0 或 1
#
#
#
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        tmp = 0
        ans = []
        for i in A:
            tmp *= 2
            if i:
                tmp += 1
            tmp %= 5    # 只需要维护余数部分
            if tmp == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans

if __name__ == "__main__":
    s = Solution().prefixesDivBy5([0,1,1])
    print(s)

