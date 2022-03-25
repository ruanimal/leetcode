# -*- coding:utf-8 -*-

# <SUBID:197176793,UPDATE:20220325>
# English:
# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
# You may return the answer in any order.
# Example 1:
# Input: n = 4, k = 2 Output: [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
# Example 2:
# Input: n = 1, k = 1 Output: [[1]]
# Constraints:
# 1 <= n <= 20
# 1 <= k <= n
#
# 中文:
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。
# 示例 1：
# 输入：n = 4, k = 2 输出： [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
# 示例 2：
# 输入：n = 1, k = 1 输出：[[1]]
# 提示：
# 1 <= n <= 20
# 1 <= k <= n


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def backtrack(start, k, res, path):
            if k == 0:
                res.append(path[:])
                return
            for i in range(start, n+1):
                # 组合的话, 为了防止重复, 已遍历的数字不要重新遍历
                path.append(i)
                backtrack(path[-1]+1, k-1, res, path)
                path.pop()

        if (n < k) or n == 0 or k == 0:
            return []
        res = []
        backtrack(1, k, res, [])
        return res

if __name__ == "__main__":
    s = Solution().combine(4,2)
    print(s)

