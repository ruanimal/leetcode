# -*- coding:utf-8 -*-

# <SUBID:16375522,UPDATE:20220325>
# English:
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
# For example, the below binary watch reads "4:51".
# Given an integer turnedOn which represents the number of LEDs that are currently on, return all possible times the watch could represent. You may return the answer in any order.
# The hour must not contain a leading zero.
# For example, "01:00" is not valid. It should be "1:00".
# The minute must be consist of two digits and may contain a leading zero.
# For example, "10:2" is not valid. It should be "10:02".
# Example 1:
# Input: turnedOn = 1 Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
# Example 2:
# Input: turnedOn = 9 Output: []
# Constraints:
# 0 <= turnedOn <= 10
#
# 中文:
# 二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或 1，最低位在右侧。
# 例如，下面的二进制手表读取 "3:25" 。
# （图源：WikiMedia - Binary clock samui moon.jpg ，许可协议：Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) ）
# 给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 按任意顺序 返回答案。
# 小时不会以零开头：
# 例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
# 分钟必须由两位数组成，可能会以零开头：
# 例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。
# 示例 1：
# 输入：turnedOn = 1 输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
# 示例 2：
# 输入：turnedOn = 9 输出：[]
# 提示：
# 0 <= turnedOn <= 10


#
# @lc app=leetcode.cn id=401 lang=python
#
# [401] 二进制手表
#
# https://leetcode-cn.com/problems/binary-watch/description/
#
# algorithms
# Easy (44.97%)
# Total Accepted:    2.9K
# Total Submissions: 6.5K
# Testcase Example:  '0'
#
# 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
#
# 每个 LED 代表一个 0 或 1，最低位在右侧。
#
#
#
# 例如，上面的二进制手表读取 “3:25”。
#
# 给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
#
# 案例:
#
#
# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16",
# "0:32"]
#
#
#
# 注意事项:
#
#
# 输出的顺序没有要求。
# 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
# 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
#
#
#
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        for i in range(2**10):
            if '{:b}'.format(i).count('1') == num:
                hour, minute = i >> 6, i & 0b111111
                if hour >= 12 or minute >= 60:
                    continue
                tmp = '{}:{:0>2}'.format(hour, minute)
                ret.append(tmp)
        return ret

if __name__ == "__main__":
    s = Solution().readBinaryWatch(4)
    print(s)

