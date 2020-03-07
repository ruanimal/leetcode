# -*- coding:utf-8 -*-


# English:
# Design a HashSet without using any built-in hash table libraries.
# To be specific, your design should include these functions:
# add(value): Insert a value into the HashSet.
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
#
# Example:
# MyHashSet hashSet = new MyHashSet(); hashSet.add(1);         hashSet.add(2);         hashSet.contains(1);    // returns true hashSet.contains(3);    // returns false (not found) hashSet.add(2);           hashSet.contains(2);    // returns true hashSet.remove(2);           hashSet.contains(2);    // returns false (already removed)
#
# Note:
# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
#
# 中文:
# 不使用任何内建的哈希表库设计一个哈希集合
# 具体地说，你的设计应该包含以下的功能
# add(value)：向哈希集合中插入一个值。
# contains(value) ：返回哈希集合中是否存在这个值。
# remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
#
# 示例:
# MyHashSet hashSet = new MyHashSet(); hashSet.add(1);         hashSet.add(2);         hashSet.contains(1);    // 返回 true hashSet.contains(3);    // 返回 false (未找到) hashSet.add(2);           hashSet.contains(2);    // 返回 true hashSet.remove(2);           hashSet.contains(2);    // 返回 false (已经被删除)
#
# 注意：
# 所有的值都在 [0, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希集合库。


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


