# -*- coding:utf-8 -*-

# <SUBID:19455923,UPDATE:20230205>
# English:
# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
# Note that you do not have any change in hand at first.
# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
# Example 1:
# Input: bills = [5,5,5,10,20] Output: true Explanation: From the first 3 customers, we collect three $5 bills in order. From the fourth customer, we collect a $10 bill and give back a $5. From the fifth customer, we give a $10 bill and a $5 bill. Since all customers got correct change, we output true.
# Example 2:
# Input: bills = [5,5,10,10,20] Output: false Explanation: From the first two customers in order, we collect two $5 bills. For the next two customers in order, we collect a $10 bill and give back a $5 bill. For the last customer, we can not give the change of $15 back because we only have two $10 bills. Since not every customer received the correct change, the answer is false.
# Constraints:
# 1 <= bills.length <= 105
# bills[i] is either 5, 10, or 20.
#
# 中文:
# 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
# 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
# 注意，一开始你手头没有任何零钱。
# 给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
# 示例 1：
# 输入：bills = [5,5,5,10,20] 输出：true 解释： 前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。 第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。 第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。 由于所有客户都得到了正确的找零，所以我们输出 true。
# 示例 2：
# 输入：bills = [5,5,10,10,20] 输出：false 解释： 前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。 对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。 对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。 由于不是每位顾客都得到了正确的找零，所以答案是 false。
# 提示：
# 1 <= bills.length <= 105
# bills[i] 不是 5 就是 10 或是 20


#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills:
            return

        coins_map = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                coins_map[5] += 1
            elif bill == 10:
                if coins_map[5] >= 1:
                    coins_map[5] -= 1
                    coins_map[10] += 1
                else:
                    return False
            elif bill == 20:
                if coins_map[10] >= 1 and coins_map[5] >= 1:
                    coins_map[10] -= 1
                    coins_map[5] -= 1
                    coins_map[20] += 1
                elif coins_map[5] >= 3:
                    coins_map[5] -= 3
                    coins_map[20] += 1
                else:
                    return False
        return True

if __name__ == "__main__":
    s = Solution().lemonadeChange([5,5,5,10,20])
    print(s)

