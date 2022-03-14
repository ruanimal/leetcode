# -*- coding:utf-8 -*-


# English:
# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
# Example 1:
# Input: nums = [1,2,1,3,2,5] Output: [3,5] Explanation: [5, 3] is also a valid answer.
# Example 2:
# Input: nums = [-1,0] Output: [-1,0]
# Example 3:
# Input: nums = [0,1] Output: [1,0]
# Constraints:
# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each integer in nums will appear twice, only two integers will appear once.
#
# 中文:
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
# 示例 1：
# 输入：nums = [1,2,1,3,2,5] 输出：[3,5] 解释：[5, 3] 也是有效的答案。
# 示例 2：
# 输入：nums = [-1,0] 输出：[-1,0]
# 示例 3：
# 输入：nums = [0,1] 输出：[1,0]
# 提示：
# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# 除两个只出现一次的整数外，nums 中的其他数字都出现两次


#
# @lc app=leetcode.cn id=260 lang=python
#
# [260] 只出现一次的数字 III
#
# https://leetcode-cn.com/problems/single-number-iii/description/
#
# algorithms
# Medium (65.93%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 10.2K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
#
# 示例 :
#
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
#
# 注意：
#
#
# 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
# 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
#
#
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        进行一次异或操作，a, b 代表最后结果，则xor = a ^ b
        xor & (~(xor-1)) 取得a ^ b 的结果的最后一个1, 记为mask
        mask代表这一个位， a和b中有且只有一个为1
        通过mask & i, 可以将nums分为两个部分，这一位为0，和这一位为1，a和b分别在其中一组中
        对每一类进行按位异或，得到最终结果a，b
        """
        xor = 0
        for i in nums:
            xor ^= i
        mask = xor & (~(xor-1))
        ans = [0, 0]
        for i in nums:
            if mask & i == mask:
                ans[0] ^= i
            else:
                ans[1] ^= i
        return ans

if __name__ == "__main__":
    s = Solution().singleNumber([1,1,2,3,4,4])
    print(s)

