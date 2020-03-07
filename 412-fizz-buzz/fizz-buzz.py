# -*- coding:utf-8 -*-


# English:
# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
# Example:
# n = 15, Return: [ "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz" ]
#
# 中文:
# 写一个程序，输出从 1 到 n 数字的字符串表示。
# 1. 如果 n 是3的倍数，输出“Fizz”；
# 2. 如果 n 是5的倍数，输出“Buzz”；
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
# 示例：
# n = 15, 返回: [ "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz" ]


#
# @lc app=leetcode.cn id=412 lang=python
#
# [412] Fizz Buzz
#
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 正常版本
        # ans = []
        # for i in range(1, n+1):
        #     if i % 15 == 0:
        #         ans.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         ans.append("Fizz")
        #     elif i % 5 == 0:
        #         ans.append("Buzz")
        #     else:
        #         ans.append(str(i))
        # return ans

        bases = ["FizzBuzz", "", "", "Fizz", "", "Buzz", "Fizz", "", "", "Fizz", "Buzz", "", "Fizz", "", ""]   # [15, 1-14]
        ans = []
        for i in range(1, n+1):
            t = i % 15
            if bases[t]:
                ans.append(bases[t])
            else:
                ans.append(str(i))
        return ans

if __name__ == "__main__":
    s = Solution().fizzBuzz(15)
    print(s)


