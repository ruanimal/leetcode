# -*- coding:utf-8 -*-

# <SUBID:17941989,UPDATE:20220325>
# English:
# A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.
# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain in the input. You may return the answer in any order.
# Example 1:
# Input: cpdomains = ["9001 discuss.leetcode.com"] Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"] Explanation: We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
# Example 2:
# Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"] Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"] Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
# Constraints:
# 1 <= cpdomain.length <= 100
# 1 <= cpdomain[i].length <= 100
# cpdomain[i] follows either the "repi d1i.d2i.d3i" format or the "repi d1i.d2i" format.
# repi is an integer in the range [1, 104].
# d1i, d2i, and d3i consist of lowercase English letters.
#
# 中文:
# 网站域名 "discuss.leetcode.com" 由多个子域名组成。顶级域名为 "com" ，二级域名为 "leetcode.com" ，最低一级为 "discuss.leetcode.com" 。当访问域名 "discuss.leetcode.com" 时，同时也会隐式访问其父域名 "leetcode.com" 以及 "com" 。
# 计数配对域名 是遵循 "rep d1.d2.d3" 或 "rep d1.d2" 格式的一个域名表示，其中 rep 表示访问域名的次数，d1.d2.d3 为域名本身。
# 例如，"9001 discuss.leetcode.com" 就是一个 计数配对域名 ，表示 discuss.leetcode.com 被访问了 9001 次。
# 给你一个 计数配对域名 组成的数组 cpdomains ，解析得到输入中每个子域名对应的 计数配对域名 ，并以数组形式返回。可以按 任意顺序 返回答案。
# 示例 1：
# 输入：cpdomains = ["9001 discuss.leetcode.com"] 输出：["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"] 解释：例子中仅包含一个网站域名："discuss.leetcode.com"。 按照前文描述，子域名 "leetcode.com" 和 "com" 都会被访问，所以它们都被访问了 9001 次。
# 示例 2：
# 输入：cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"] 输出：["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"] 解释：按照前文描述，会访问 "google.mail.com" 900 次，"yahoo.com" 50 次，"intel.mail.com" 1 次，"wiki.org" 5 次。 而对于父域名，会访问 "mail.com" 900 + 1 = 901 次，"com" 900 + 50 + 1 = 951 次，和 "org" 5 次。
# 提示：
# 1 <= cpdomain.length <= 100
# 1 <= cpdomain[i].length <= 100
# cpdomain[i] 会遵循 "repi d1i.d2i.d3i" 或 "repi d1i.d2i" 格式
# repi 是范围 [1, 104] 内的一个整数
# d1i、d2i 和 d3i 由小写英文字母组成


#
# @lc app=leetcode.cn id=811 lang=python
#
# [811] 区间子数组个数
#
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ret_map = {}
        for i in cpdomains:
            nums, domains = i.split()
            domains = domains.split('.')
            for idx in range(len(domains)-1, -1, -1):
                key = '.'.join(domains[idx:])
                ret_map[key] = ret_map.get(key, 0) + int(nums)
        return ['{} {}'.format(v, k) for k, v in ret_map.items()]

if __name__ == "__main__":
    s = Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    print(s)

