# -*- coding:utf-8 -*-

# <SUBID:19988437,UPDATE:20230205>
# English:
# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
# Example 1:
# Input: name = "alex", typed = "aaleex" Output: true Explanation: 'a' and 'e' in 'alex' were long pressed.
# Example 2:
# Input: name = "saeed", typed = "ssaaedd" Output: false Explanation: 'e' must have been pressed twice, but it was not in the typed output.
# Constraints:
# 1 <= name.length, typed.length <= 1000
# name and typed consist of only lowercase English letters.
#
# 中文:
# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
# 示例 1：
# 输入：name = "alex", typed = "aaleex" 输出：true 解释：'alex' 中的 'a' 和 'e' 被长按。
# 示例 2：
# 输入：name = "saeed", typed = "ssaaedd" 输出：false 解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
# 提示：
# 1 <= name.length, typed.length <= 1000
# name 和 typed 的字符都是小写字母


#
# @lc app=leetcode.cn id=925 lang=python
#
# [925] 根据前序和后序遍历构造二叉树
#
# https://leetcode-cn.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (40.47%)
# Likes:    29
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 7K
# Testcase Example:  '"alex"\n"aaleex"'
#
# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
#
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
#
#
#
# 示例 1：
#
# 输入：name = "alex", typed = "aaleex"
# 输出：true
# 解释：'alex' 中的 'a' 和 'e' 被长按。
#
#
# 示例 2：
#
# 输入：name = "saeed", typed = "ssaaedd"
# 输出：false
# 解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
#
#
# 示例 3：
#
# 输入：name = "leelee", typed = "lleeelee"
# 输出：true
#
#
# 示例 4：
#
# 输入：name = "laiden", typed = "laiden"
# 输出：true
# 解释：长按名字中的字符并不是必要的。
#
#
#
#
# 提示：
#
#
# name.length <= 1000
# typed.length <= 1000
# name 和 typed 的字符都是小写字母。
#
#
#
#
#
#
#
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        def seq_count(name):
            if not name:
                return []
            count = 1
            ans = []
            for i in range(1, len(name)):
                if name[i-1] != name[i]:
                    ans.append(count)
                    count = 1
                else:
                    count += 1
            ans.append(count)
            return ans

        a, b = seq_count(name), seq_count(typed)
        if len(a) != len(b):
            return False
        for i, j in zip(a, b):
            if i > j:
                return False
        return True

if __name__ == "__main__":
    s = Solution().isLongPressedName(name = "alex", typed = "aaleex")
    print(s)
    s = Solution().isLongPressedName(name = "saeed", typed = "ssaaedd")
    print(s)
    s = Solution().isLongPressedName(name = "laiden", typed = "laiden")
    print(s)

