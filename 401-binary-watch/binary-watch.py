# -*- coding:utf-8 -*-


# English:
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.
# For example, the above binary watch reads "3:25".
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
# Example:
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Note:
#
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
#
# 中文:
# 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
# 每个 LED 代表一个 0 或 1，最低位在右侧。
# 例如，上面的二进制手表读取 “3:25”。
# 给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
# 案例:
# 输入: n = 1 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# 注意事项:
# 输出的顺序没有要求。
# 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
# 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。


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

