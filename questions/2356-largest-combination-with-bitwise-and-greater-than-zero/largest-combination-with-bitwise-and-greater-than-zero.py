# -*- coding:utf-8 -*-

# <SUBID:315318926,UPDATE:20230205>
# English:
# The bitwise AND of an array nums is the bitwise AND of all integers in nums.
# For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
# Also, for nums = [7], the bitwise AND is 7.
# You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.
# Return the size of the largest combination of candidates with a bitwise AND greater than 0.
# Example 1:
# Input: candidates = [16,17,71,62,12,24,14] Output: 4 Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0. The size of the combination is 4. It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0. Note that more than one combination may have the largest size. For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.
# Example 2:
# Input: candidates = [8,8] Output: 2 Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0. The size of the combination is 2, so we return 2.
# Constraints:
# 1 <= candidates.length <= 105
# 1 <= candidates[i] <= 107
#
# 中文:
# 对数组 nums 执行 按位与 相当于对数组 nums 中的所有整数执行 按位与 。
# 例如，对 nums = [1, 5, 3] 来说，按位与等于 1 & 5 & 3 = 1 。
# 同样，对 nums = [7] 而言，按位与等于 7 。
# 给你一个正整数数组 candidates 。计算 candidates 中的数字每种组合下 按位与 的结果。 candidates 中的每个数字在每种组合中只能使用 一次 。
# 返回按位与结果大于 0 的 最长 组合的长度。
# 示例 1：
# 输入：candidates = [16,17,71,62,12,24,14] 输出：4 解释：组合 [16,17,62,24] 的按位与结果是 16 & 17 & 62 & 24 = 16 > 0 。 组合长度是 4 。 可以证明不存在按位与结果大于 0 且长度大于 4 的组合。 注意，符合长度最大的组合可能不止一种。 例如，组合 [62,12,24,14] 的按位与结果是 62 & 12 & 24 & 14 = 8 > 0 。
# 示例 2：
# 输入：candidates = [8,8] 输出：2 解释：最长组合是 [8,8] ，按位与结果 8 & 8 = 8 > 0 。 组合长度是 2 ，所以返回 2 。
# 提示：
# 1 <= candidates.length <= 105
# 1 <= candidates[i] <= 107


from collections import Counter

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0] * 24
        for num in candidates:
            for i in range(24):
                count[i] += (num >> i) & 1
        return max(count)
