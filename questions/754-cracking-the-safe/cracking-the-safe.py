# -*- coding:utf-8 -*-

# <SUBID:319349087,UPDATE:20230205>
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
# 有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位都是范围 [0, k - 1] 中的一个数字。
# 保险箱有一种特殊的密码校验方法，你可以随意输入密码序列，保险箱会自动记住 最后 n 位输入 ，如果匹配，则能够打开保险箱。
# 例如，正确的密码是 "345" ，并且你输入的是 "012345" ：
# 输入 0 之后，最后 3 位输入是 "0" ，不正确。
# 输入 1 之后，最后 3 位输入是 "01" ，不正确。
# 输入 2 之后，最后 3 位输入是 "012" ，不正确。
# 输入 3 之后，最后 3 位输入是 "123" ，不正确。
# 输入 4 之后，最后 3 位输入是 "234" ，不正确。
# 输入 5 之后，最后 3 位输入是 "345" ，正确，打开保险箱。
# 在只知道密码位数 n 和范围边界 k 的前提下，请你找出并返回确保在输入的 某个时刻 能够打开保险箱的任一 最短 密码序列 。
# 示例 1：
# 输入：n = 1, k = 2 输出："10" 解释：密码只有 1 位，所以输入每一位就可以。"01" 也能够确保打开保险箱。
# 示例 2：
# 输入：n = 2, k = 2 输出："01100" 解释：对于每种可能的密码： - "00" 从第 4 位开始输入。 - "01" 从第 1 位开始输入。 - "10" 从第 3 位开始输入。 - "11" 从第 2 位开始输入。 因此 "01100" 可以确保打开保险箱。"01100"、"10011" 和 "11001" 也可以确保打开保险箱。
# 提示：
# 1 <= n <= 4
# 1 <= k <= 10
# 1 <= kn <= 4096


#
# @lc app=leetcode.cn id=753 lang=python3
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
    def crackSafe(self, n: int, k: int) -> str:
        """暴力回溯法
        """
        if n == 1:
            return ''.join(str(i) for i in range(k))
        ans = [0 for _ in range(n)]
        total = k ** n
        visited = set()
        visited.add(tuple(ans))
        self.dfs(ans, total, visited, n, k)
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

'''leetcode高分答案
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        这道题说的是给了k个数字，值为0到k-1，让我们组成n位密码。我们可以发现，为了尽可能的使钥匙串变短，所以我们的密码之间尽可能要相互重叠，比如00和01，就共享一个0，如果是3个数，012和120共享两个数”12”，那么我们可以发现，两个长度为n的密码最好能共享n-1个数字，这样累加出来的钥匙串肯定是最短的。

密码共有n位，每一个位可以有k个数字，那么总共不同的密码总数就有k的n次方个。我们的思路是先从n位都是0的密码开始，取出钥匙串的最后n个数字，然后将最后一个数字依次换成其他数字，我们用一个HashSet来记录所有遍历过的密码，这样如果不在集合中，说明是一个新密码，而生成这个新密码也只是多加了一个数字，这样能保证我们的钥匙串最短，这是一种贪婪的解法
        """
        res='0'*n
        s=set()
        s.add(res)
        for i in range(k**n):
            tmp=res[len(res)-n+1:]
            for j in range(k-1,-1,-1):
                key=tmp+str(j)
                if key not in s:
                    res+=str(j)
                    s.add(key)
                    break
        return res

'''

if __name__ == "__main__":
    print(test_solution())


