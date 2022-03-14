# -*- coding:utf-8 -*-


# English:
# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.
# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
# Example 1:
# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"] Output: 2 Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
# Example 2:
# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"] Output: 3
# Constraints:
# 1 <= emails.length <= 100
# 1 <= emails[i].length <= 100
# emails[i] consist of lowercase English letters, '+', '.' and '@'.
# Each emails[i] contains exactly one '@' character.
# All local and domain names are non-empty.
# Local names do not start with a '+' character.
# Domain names end with the ".com" suffix.
#
# 中文:
# 每个 有效电子邮件地址 都由一个 本地名 和一个 域名 组成，以 '@' 符号分隔。除小写字母之外，电子邮件地址还可以含有一个或多个 '.' 或 '+' 。
# 例如，在 alice@leetcode.com中， alice 是 本地名 ，而 leetcode.com 是 域名 。
# 如果在电子邮件地址的 本地名 部分中的某些字符之间添加句点（'.'），则发往那里的邮件将会转发到本地名中没有点的同一地址。请注意，此规则 不适用于域名 。
# 例如，"alice.z@leetcode.com” 和 “alicez@leetcode.com” 会转发到同一电子邮件地址。
# 如果在 本地名 中添加加号（'+'），则会忽略第一个加号后面的所有内容。这允许过滤某些电子邮件。同样，此规则 不适用于域名 。
# 例如 m.y+name@email.com 将转发到 my@email.com。
# 可以同时使用这两个规则。
# 给你一个字符串数组 emails，我们会向每个 emails[i] 发送一封电子邮件。返回实际收到邮件的不同地址数目。
# 示例 1：
# 输入：emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"] 输出：2 解释：实际收到邮件的是 "testemail@leetcode.com" 和 "testemail@lee.tcode.com"。
# 示例 2：
# 输入：emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"] 输出：3
#
# 提示：
# 1 <= emails.length <= 100
# 1 <= emails[i].length <= 100
# emails[i] 由小写英文字母、'+'、'.' 和 '@' 组成
# 每个 emails[i] 都包含有且仅有一个 '@' 字符
# 所有本地名和域名都不为空
# 本地名不会以 '+' 字符作为开头


#
# @lc app=leetcode.cn id=929 lang=python
#
# [929] 特殊等价字符串组
#
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ret = set()
        for email in emails:
            at_idx = email.index('@')
            tmp = []
            for idx, i in enumerate(email):
                if i == '.':
                    continue
                if (i == '+' or idx >= at_idx):
                    break
                tmp.append(i)
            tmp.append(email[at_idx:])
            ret.add(''.join(tmp))
        # print(ret)
        return len(ret)

if __name__ == "__main__":
    s = Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
    print(s)

