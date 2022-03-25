# -*- coding:utf-8 -*-

# <SUBID:23978934,UPDATE:20220325>
# English:
# There is a safe protected by a password. The password is a sequence of n digits where each digit can be in the range [0, k - 1].
# The safe has a peculiar way of checking the password. When you enter in a sequence, it checks the most recent n digits that were entered each time you type a digit.
# For example, the correct password is "345" and you enter in "012345":
# After typing 0, the most recent 3 digits is "0", which is incorrect.
# After typing 1, the most recent 3 digits is "01", which is incorrect.
# After typing 2, the most recent 3 digits is "012", which is incorrect.
# After typing 3, the most recent 3 digits is "123", which is incorrect.
# After typing 4, the most recent 3 digits is "234", which is incorrect.
# After typing 5, the most recent 3 digits is "345", which is correct and the safe unlocks.
# Return any string of minimum length that will unlock the safe at some point of entering it.
# Example 1:
# Input: n = 1, k = 2 Output: "10" Explanation: The password is a single digit, so enter each digit. "01" would also unlock the safe.
# Example 2:
# Input: n = 2, k = 2 Output: "01100" Explanation: For each possible password: - "00" is typed in starting from the 4th digit. - "01" is typed in starting from the 1st digit. - "10" is typed in starting from the 3rd digit. - "11" is typed in starting from the 2nd digit. Thus "01100" will unlock the safe. "01100", "10011", and "11001" would also unlock the safe.
# Constraints:
# 1 <= n <= 4
# 1 <= k <= 10
# 1 <= kn <= 4096
#
# 中文:
# 有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。
# 你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。
# 举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.
# 请返回一个能打开保险箱的最短字符串。
# 示例1:
# 输入: n = 1, k = 2 输出: "01" 说明: "10"也可以打开保险箱。
# 示例2:
# 输入: n = 2, k = 2 输出: "00110" 说明: "01100", "10011", "11001" 也能打开保险箱。
# 提示：
# n 的范围是 [1, 4]。
# k 的范围是 [1, 10]。
# k^n 最大可能为 4096。


#
# @lc app=leetcode.cn id=753 lang=python
#
# [753] 破解保险箱
#
# https://leetcode-cn.com/problems/cracking-the-safe/description/
#
# algorithms
# Hard (48.67%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    224
# Total Submissions: 456
# Testcase Example:  '1\n1'
#
# 有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。
#
# 你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。
#
# 举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.
#
# 请返回一个能打开保险箱的最短字符串。
#
#
#
# 示例1:
#
# 输入: n = 1, k = 2
# 输出: "01"
# 说明: "10"也可以打开保险箱。
#
#
#
#
# 示例2:
#
# 输入: n = 2, k = 2
# 输出: "00110"
# 说明: "01100", "10011", "11001" 也能打开保险箱。
#
#
#
#
# 提示：
#
#
# n 的范围是 [1, 4]。
# k 的范围是 [1, 10]。
# k^n 最大可能为 4096。
#
#
#
#
#
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return ''.join(str(i) for i in range(k))
        ans = [0 for _ in range(n)]
        total = k ** n
        visited = set()
        visited.add(tuple(ans))
        self.dfs(ans, total, visited, n, k)
        #print(ans)
        return ''.join(str(i) for i in ans)

    @staticmethod
    def dfs(ans, goal, visited, n, k):
        if len(visited) == goal:
            return True
        prev = ans[-n+1:]
        for i in range(0, k):
            prev.append(i)
            next_ = tuple(prev)
            if next_ not in visited:
                visited.add(next_)
                ans.append(i)
                if Solution.dfs(ans, goal, visited, n, k):
                    return True
                else:
                    visited.remove(next_)
                    ans.pop()
        return False


def test_solution():
    from itertools import product
    ans = Solution().crackSafe(2, 5)
    print(ans)
    for i in product(range(5), repeat=2):
        tmp = ''.join(str(x) for x in i)
        if tmp not in ans:
            print(tmp)
            return False
    return True

if __name__ == "__main__":
    print(test_solution())


