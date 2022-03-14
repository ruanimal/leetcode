# -*- coding:utf-8 -*-


# English:
# You are given a list of songs where the ith song has a duration of time[i] seconds.
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
# Example 1:
# Input: time = [30,20,150,100,40] Output: 3 Explanation: Three pairs have a total duration divisible by 60: (time[0] = 30, time[2] = 150): total duration 180 (time[1] = 20, time[3] = 100): total duration 120 (time[1] = 20, time[4] = 40): total duration 60
# Example 2:
# Input: time = [60,60,60] Output: 3 Explanation: All three pairs have a total duration of 120, which is divisible by 60.
# Constraints:
# 1 <= time.length <= 6 * 104
# 1 <= time[i] <= 500
#
# 中文:
# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
# 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望下标数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。
# 示例 1：
# 输入：time = [30,20,150,100,40] 输出：3 解释：这三对的总持续时间可被 60 整除： (time[0] = 30, time[2] = 150): 总持续时间 180 (time[1] = 20, time[3] = 100): 总持续时间 120 (time[1] = 20, time[4] = 40): 总持续时间 60
# 示例 2：
# 输入：time = [60,60,60] 输出：3 解释：所有三对的总持续时间都是 120，可以被 60 整除。
# 提示：
# 1 <= time.length <= 6 * 104
# 1 <= time[i] <= 500


#
# @lc app=leetcode.cn id=1013 lang=python
#
# [1013] 斐波那契数
#
# https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Easy (39.46%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 5.4K
# Testcase Example:  '[30,20,150,100,40]'
#
# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
#
# 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字  i < j 且有 (time[i] + time[j]) %
# 60 == 0。
#
#
#
# 示例 1：
#
# 输入：[30,20,150,100,40]
# 输出：3
# 解释：这三对的总持续时间可被 60 整数：
# (time[0] = 30, time[2] = 150): 总持续时间 180
# (time[1] = 20, time[3] = 100): 总持续时间 120
# (time[1] = 20, time[4] = 40): 总持续时间 60
#
#
# 示例 2：
#
# 输入：[60,60,60]
# 输出：3
# 解释：所有三对的总持续时间都是 120，可以被 60 整数。
#
#
#
#
# 提示：
#
#
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500
#
#
#
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # # v1. 暴力法， 复杂度太高
        # tmp = []
        # ans = 0
        # for j in range(1, len(time)):
        #     for i in range(j):
        #         if (time[i] + time[j]) % 60 == 0:
        #             tmp.append((time[i], time[j]))
        #             ans += 1
        # print(sorted(tmp))
        # return ans

        # # v2. 用dict做优化， 复杂度还是太高
        # ans = 0
        # tmp_map = {}
        # for idx, i in enumerate(time):
        #     tmp_map.setdefault(i % 60, []).append(idx)
        # for idx, a in enumerate(time):
        #     a = (a % 60)
        #     if a == 0:
        #         b = 0
        #     else:
        #         b = 60 - a
        #     if b not in tmp_map: continue
        #     for idx2, j in enumerate(tmp_map[b]):
        #         if j > idx:
        #             ans += (len(tmp_map[b])-idx2)
        #             break
        # return ans

        ans = 0
        tmp_map = {}
        for idx, a in enumerate(time):
            b = -a % 60  # -20 % 60 = 40, 求另一半，比60-a准确
            ans += len(tmp_map.get(b, []))
            tmp_map.setdefault(a % 60, []).append(idx)
        return ans


if __name__ == "__main__":
    pass
    # s = Solution().numPairsDivisibleBy60([30,20,150,100,40])
    # print(s)
    # s = Solution().numPairsDivisibleBy60([60,60,60])
    # print(s)
    s = Solution().numPairsDivisibleBy60([459,42,469,132,37,460,143,1,144,127,398,82,370,464,14,85,321,358,205,14,264,289,183,93,56,126,413,140,441,446,445,378,258,119,385,226,8,93,476,265,115,86,360,92,396,407,458,58,65,397,381,32,228,37,319,220,73,328,162,458,231,219,481,387,423,256,252,36,309,395,471,4,225,146,188,182,347,82,21,292,91,144,387,263,206,452,197,192,324,257,370,28,440,180,294])
    print(s)


