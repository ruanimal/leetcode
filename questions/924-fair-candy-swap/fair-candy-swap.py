# -*- coding:utf-8 -*-

# <SUBID:319573151,UPDATE:20230205>
# English:
# Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.
# Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.
# Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.
# Example 1:
# Input: aliceSizes = [1,1], bobSizes = [2,2] Output: [1,2]
# Example 2:
# Input: aliceSizes = [1,2], bobSizes = [2,3] Output: [1,2]
# Example 3:
# Input: aliceSizes = [2], bobSizes = [1,3] Output: [2,3]
# Constraints:
# 1 <= aliceSizes.length, bobSizes.length <= 104
# 1 <= aliceSizes[i], bobSizes[j] <= 105
# Alice and Bob have a different total number of candies.
# There will be at least one valid answer for the given input.
#
# 中文:
# 爱丽丝和鲍勃拥有不同总数量的糖果。给你两个数组 aliceSizes 和 bobSizes ，aliceSizes[i] 是爱丽丝拥有的第 i 盒糖果中的糖果数量，bobSizes[j] 是鲍勃拥有的第 j 盒糖果中的糖果数量。
# 两人想要互相交换一盒糖果，这样在交换之后，他们就可以拥有相同总数量的糖果。一个人拥有的糖果总数量是他们每盒糖果数量的总和。
# 返回一个整数数组 answer，其中 answer[0] 是爱丽丝必须交换的糖果盒中的糖果的数目，answer[1] 是鲍勃必须交换的糖果盒中的糖果的数目。如果存在多个答案，你可以返回其中 任何一个 。题目测试用例保证存在与输入对应的答案。
# 示例 1：
# 输入：aliceSizes = [1,1], bobSizes = [2,2] 输出：[1,2]
# 示例 2：
# 输入：aliceSizes = [1,2], bobSizes = [2,3] 输出：[1,2]
# 示例 3：
# 输入：aliceSizes = [2], bobSizes = [1,3] 输出：[2,3]
# 示例 4：
# 输入：aliceSizes = [1,2,5], bobSizes = [2,4] 输出：[5,4]
# 提示：
# 1 <= aliceSizes.length, bobSizes.length <= 104
# 1 <= aliceSizes[i], bobSizes[j] <= 105
# 爱丽丝和鲍勃的糖果总数量不同。
# 题目数据保证对于给定的输入至少存在一个有效答案。


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        """求和计算出两者差距"""

        set_b = set(bobSizes)
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        gap = sum_a - sum_b
        for i in aliceSizes:
            j = int((2 * i - gap) / 2)
            if j in set_b:
                return [i, j]
