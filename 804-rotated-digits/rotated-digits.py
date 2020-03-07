# -*- coding:utf-8 -*-


# English:
# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
# Now given a positive number N, how many numbers X from 1 to N are good?
# Example: Input: 10 Output: 4 Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9. Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
# N  will be in range [1, 10000].
#
# 中文:
# 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。
# 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
# 现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？
# 示例: 输入: 10 输出: 4 解释: 在[1, 10]中有四个好数： 2, 5, 6, 9。 注意 1 和 10 不是好数, 因为他们在旋转之后不变。
# 注意:
# N 的取值范围是 [1, 10000]。


#
# @lc app=leetcode.cn id=788 lang=python
#
# [788] 旋转数字
#
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        trans_map = {'1':'1', '0':'0', '8':'8', '2': '5', '5': '2', '6': '9', '9': '6'}
        for i in range(1, N+1):
            str_num = list(str(i))
            tmp = []
            for j in str_num:
                if j in trans_map:
                    tmp.append(trans_map[j])
                else:
                    break
            if len(tmp) == len(str_num) and tmp != str_num:
                count += 1
        return count

if __name__ == "__main__":
    s = Solution().rotatedDigits(10)
    print(s)


