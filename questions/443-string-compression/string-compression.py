# -*- coding:utf-8 -*-

# <SUBID:20919440,UPDATE:20220325>
# English:
# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.
# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"] Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"] Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:
# Input: chars = ["a"] Output: Return 1, and the first character of the input array should be: ["a"] Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"] Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"]. Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
# Constraints:
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
#
# 中文:
# 给你一个字符数组 chars ，请使用下述算法压缩：
# 从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
# 如果这一组长度为 1 ，则将字符追加到 s 中。
# 否则，需要向 s 追加字符，后跟这一组的长度。
# 压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。
# 请在 修改完输入数组后 ，返回该数组的新长度。
# 你必须设计并实现一个只使用常量额外空间的算法来解决此问题。
# 示例 1：
# 输入：chars = ["a","a","b","b","c","c","c"] 输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"] 解释："aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
# 示例 2：
# 输入：chars = ["a"] 输出：返回 1 ，输入数组的前 1 个字符应该是：["a"] 解释：唯一的组是“a”，它保持未压缩，因为它是一个字符。
# 示例 3：
# 输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"] 输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。 解释：由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
# 提示：
# 1 <= chars.length <= 2000
# chars[i] 可以是小写英文字母、大写英文字母、数字或符号


#
# @lc app=leetcode.cn id=443 lang=python
#
# [443] 压缩字符串
#
# https://leetcode-cn.com/problems/string-compression/description/
#
# algorithms
# Easy (33.96%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 12.9K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# 给定一组字符，使用原地算法将其压缩。
#
# 压缩后的长度必须始终小于或等于原数组长度。
#
# 数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
#
# 在完成原地修改输入数组后，返回数组的新长度。
#
#
#
# 进阶：
# 你能否仅使用O(1) 空间解决问题？
#
#
#
# 示例 1：
#
#
# 输入：
# ["a","a","b","b","c","c","c"]
#
# 输出：
# 返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]
#
# 说明：
# "aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。
#
#
# 示例 2：
#
#
# 输入：
# ["a"]
#
# 输出：
# 返回1，输入数组的前1个字符应该是：["a"]
#
# 说明：
# 没有任何字符串被替代。
#
#
# 示例 3：
#
#
# 输入：
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#
# 输出：
# 返回4，输入数组的前4个字符应该是：["a","b","1","2"]。
#
# 说明：
# 由于字符"a"不重复，所以不会被压缩。"bbbbbbbbbbbb"被“b12”替代。
# 注意每个数字在数组中都有它自己的位置。
#
#
# 注意：
#
#
# 所有字符都有一个ASCII值在[35, 126]区间内。
# 1 <= len(chars) <= 1000。
#
#
#
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cnt = 1
        cur_char = chars[0]
        idx = 1
        while idx < len(chars):
            if chars[idx] == cur_char:
                cnt += 1
                idx += 1
            else:
                if cnt > 1:
                    chars[idx-cnt:idx] = [cur_char] + list(str(cnt))
                    idx = idx - cnt + len(str(cnt)) + 1
                cnt = 1
                cur_char = chars[idx]
                idx += 1
        if cnt > 1:
            chars[idx-cnt:idx] = [cur_char] + list(str(cnt))
        # print(chars)
        return len(chars)

if __name__ == "__main__":
    s = Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b", "c", 'c'])
    print(s)
    s = Solution().compress(["a","b"])
    print(s)
    s = Solution().compress(["a"])
    print(s)
    s = Solution().compress(["p","p","p","p","m","m","b","b","b","b","b","u","u","r","r","u","n","n","n","n","n","n","n","n","n","n","n","u","u","u","u","a","a","u","u","r","r","r","s","s","a","a","y","y","y","g","g","g","g","g"])
    print(s)

