# -*- coding:utf-8 -*-


# English:
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
# Custom Judge:
# The judge will test your solution with the following code:
# int[] nums = [...]; // Input array int[] expectedNums = [...]; // The expected answer with correct length int k = removeDuplicates(nums); // Calls your implementation assert k == expectedNums.length; for (int i = 0; i < k; i++) { assert nums[i] == expectedNums[i]; }
# If all assertions pass, then your solution will be accepted.
# Example 1:
# Input: nums = [1,1,2] Output: 2, nums = [1,2,_] Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4] Output: 5, nums = [0,1,2,3,4,_,_,_,_,_] Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
# Constraints:
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
#
# 中文:
# 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
# 由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 k 个元素，那么 nums 的前 k 个元素应该保存最终结果。
# 将最终结果插入 nums 的前 k 个位置后返回 k 。
# 不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
# 判题标准:
# 系统会用下面的代码来测试你的题解:
# int[] nums = [...]; // 输入数组 int[] expectedNums = [...]; // 长度正确的期望答案 int k = removeDuplicates(nums); // 调用 assert k == expectedNums.length; for (int i = 0; i < k; i++) { assert nums[i] == expectedNums[i]; }
# 如果所有断言都通过，那么您的题解将被 通过。
# 示例 1：
# 输入：nums = [1,1,2] 输出：2, nums = [1,2,_] 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
# 示例 2：
# 输入：nums = [0,0,1,1,1,2,2,3,3,4] 输出：5, nums = [0,1,2,3,4] 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
# 提示：
# 0 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums 已按 升序 排列


#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (42.44%)
# Total Accepted:    97.4K
# Total Submissions: 224.9K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1:
#
# 给定数组 nums = [1,1,2],
#
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
#
# 你不需要考虑数组中超出新长度后面的元素。
#
# 示例 2:
#
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
#
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
#
# 你不需要考虑数组中超出新长度后面的元素。
#
#
# 说明:
#
# 为什么返回数值是整数，但输出的答案是数组呢?
#
# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
#
# 你可以想象内部操作如下:
#
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
#
#
#


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length

        slow, fast = 1, 1
        while fast < length:
            if nums[fast] != nums[slow-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

if __name__ == '__main__':
    s = Solution()
    case = [0,0,1,1,1,2,2,3,3,4]
    res = s.removeDuplicates(case)
    print(case[:res])

