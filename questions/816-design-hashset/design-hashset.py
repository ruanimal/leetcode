# -*- coding:utf-8 -*-

# <SUBID:16416426,UPDATE:20220325>
# English:
# Design a HashSet without using any built-in hash table libraries.
# Implement MyHashSet class:
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
# Example 1:
# Input ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"] [[], [1], [2], [1], [3], [2], [2], [2], [2]] Output [null, null, null, true, false, null, true, null, false] Explanation MyHashSet myHashSet = new MyHashSet(); myHashSet.add(1); // set = [1] myHashSet.add(2); // set = [1, 2] myHashSet.contains(1); // return True myHashSet.contains(3); // return False, (not found) myHashSet.add(2); // set = [1, 2] myHashSet.contains(2); // return True myHashSet.remove(2); // set = [1] myHashSet.contains(2); // return False, (already removed)
# Constraints:
# 0 <= key <= 106
# At most 104 calls will be made to add, remove, and contains.
#
# 中文:
# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
# 实现 MyHashSet 类：
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
# 示例：
# 输入： ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"] [[], [1], [2], [1], [3], [2], [2], [2], [2]] 输出： [null, null, null, true, false, null, true, null, false] 解释： MyHashSet myHashSet = new MyHashSet(); myHashSet.add(1); // set = [1] myHashSet.add(2); // set = [1, 2] myHashSet.contains(1); // 返回 True myHashSet.contains(3); // 返回 False ，（未找到） myHashSet.add(2); // set = [1, 2] myHashSet.contains(2); // 返回 True myHashSet.remove(2); // set = [1] myHashSet.contains(2); // 返回 False ，（已移除）
# 提示：
# 0 <= key <= 106
# 最多调用 104 次 add、remove 和 contains


#
# @lc app=leetcode.cn id=705 lang=python
#
# [705] Design HashSet
#
# https://leetcode-cn.com/problems/design-hashset/description/
#
# algorithms
# Easy (52.05%)
# Total Accepted:    3.2K
# Total Submissions: 5.9K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希集合
#
# 具体地说，你的设计应该包含以下的功能
#
#
# add(value)：向哈希集合中插入一个值。
# contains(value) ：返回哈希集合中是否存在这个值。
# remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
#
#
#
# 示例:
#
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);        
# hashSet.add(2);        
# hashSet.contains(1);    // 返回 true
# hashSet.contains(3);    // 返回 false (未找到)
# hashSet.add(2);          
# hashSet.contains(2);    // 返回 true
# hashSet.remove(2);          
# hashSet.contains(2);    // 返回  false (已经被删除)
#
#
#
# 注意：
#
#
# 所有的值都在 [1, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希集合库。
#
#
#
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [None] * 10001

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        value = 1
        hash_key = key // 100
        pair = self.data[hash_key]
        if pair is None:
            self.data[hash_key] = (key, value)
        elif isinstance(pair, tuple):
            if pair[0] == key:
                self.data[hash_key] = (key, value)
            else:
                self.data[hash_key] = [pair, (key, value)]
        else:
            for i in range(len(pair)):
                if pair[i][0] == key:
                    pair[i] = (key, value)
                    return
            pair.append((key, value))

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hash_key = key // 100
        pair = self.data[hash_key]
        if pair is None:
            return False
        elif isinstance(pair, tuple):
            if pair[0] == key:
                return True
        else:
            for i in pair:
                if i[0] == key:
                    return True
        return False

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = key // 100
        pair = self.data[hash_key]
        # print(pair)
        if pair is None:
            return
        elif isinstance(pair, tuple):
            if pair[0] == key:
                self.data[hash_key] = None
        else:
            for i in range(len(pair)):
                if pair[i][0] == key:
                    del pair[i]
                    return
        return


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


