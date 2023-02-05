# -*- coding:utf-8 -*-

# <SUBID:290175921,UPDATE:20230205>
# English:
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.
# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
# Note: You cannot rotate an envelope.
# Example 1:
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]] Output: 3 Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# Example 2:
# Input: envelopes = [[1,1],[1,1],[1,1]] Output: 1
# Constraints:
# 1 <= envelopes.length <= 105
# envelopes[i].length == 2
# 1 <= wi, hi <= 105
#
# 中文:
# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 注意：不允许旋转信封。
# 示例 1：
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]] 输出：3 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
# 示例 2：
# 输入：envelopes = [[1,1],[1,1],[1,1]] 输出：1
# 提示：
# 1 <= envelopes.length <= 105
# envelopes[i].length == 2
# 1 <= wi, hi <= 105


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num
        
        return len(f)

