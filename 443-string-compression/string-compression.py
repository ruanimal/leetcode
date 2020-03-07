# -*- coding:utf-8 -*-


# English:
# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.
# Follow up:
# Could you solve it using only O(1) extra space?
# Example 1:
# Input: ["a","a","b","b","c","c","c"] Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"] Explanation: "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
# Example 2:
# Input: ["a"] Output: Return 1, and the first 1 characters of the input array should be: ["a"] Explanation: Nothing is replaced.
# Example 3:
# Input: ["a","b","b","b","b","b","b","b","b","b","b","b","b"] Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"]. Explanation: Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12". Notice each digit has it's own entry in the array.
# Note:
# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.
#
# 中文:
# 给定一组字符，使用原地算法将其压缩。
# 压缩后的长度必须始终小于或等于原数组长度。
# 数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
# 在完成原地修改输入数组后，返回数组的新长度。
# 进阶：
# 你能否仅使用O(1) 空间解决问题？
# 示例 1：
# 输入： ["a","a","b","b","c","c","c"] 输出： 返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"] 说明： "aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。
# 示例 2：
# 输入： ["a"] 输出： 返回1，输入数组的前1个字符应该是：["a"] 说明： 没有任何字符串被替代。
# 示例 3：
# 输入： ["a","b","b","b","b","b","b","b","b","b","b","b","b"] 输出： 返回4，输入数组的前4个字符应该是：["a","b","1","2"]。 说明： 由于字符"a"不重复，所以不会被压缩。"bbbbbbbbbbbb"被“b12”替代。 注意每个数字在数组中都有它自己的位置。
# 注意：
# 所有字符都有一个ASCII值在[35, 126]区间内。
# 1 <= len(chars) <= 1000。


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

