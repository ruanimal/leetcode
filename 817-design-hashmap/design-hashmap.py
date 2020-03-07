# -*- coding:utf-8 -*-


# English:
# Design a HashMap without using any built-in hash table libraries.
# To be specific, your design should include these functions:
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
#
# Example:
# MyHashMap hashMap = new MyHashMap(); hashMap.put(1, 1);           hashMap.put(2, 2);         hashMap.get(1);            // returns 1 hashMap.get(3);            // returns -1 (not found) hashMap.put(2, 1);          // update the existing value hashMap.get(2);            // returns 1 hashMap.remove(2);          // remove the mapping for 2 hashMap.get(2);            // returns -1 (not found)
#
# Note:
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.
#
# 中文:
# 不使用任何内建的哈希表库设计一个哈希映射
# 具体地说，你的设计应该包含以下的功能
# put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
# get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
# remove(key)：如果映射中存在这个键，删除这个数值对。
#
# 示例：
# MyHashMap hashMap = new MyHashMap(); hashMap.put(1, 1);           hashMap.put(2, 2);         hashMap.get(1);            // 返回 1 hashMap.get(3);            // 返回 -1 (未找到) hashMap.put(2, 1);         // 更新已有的值 hashMap.get(2);            // 返回 1 hashMap.remove(2);         // 删除键为2的数据 hashMap.get(2);            // 返回 -1 (未找到)
#
# 注意：
# 所有的值都在 [1, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希库。


#
# @lc app=leetcode.cn id=706 lang=python
#
# [706] Design HashMap
#
# https://leetcode-cn.com/problems/design-hashmap/description/
#
# algorithms
# Easy (53.40%)
# Total Accepted:    2.6K
# Total Submissions: 4.8K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get", "remove", "get"]\n[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希映射
#
# 具体地说，你的设计应该包含以下的功能
#
#
# put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
# get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
# remove(key)：如果映射中存在这个键，删除这个数值对。
#
#
#
# 示例：
#
#
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);        
# hashMap.get(1);            // 返回 1
# hashMap.get(3);            // 返回 -1 (未找到)
# hashMap.put(2, 1);         // 更新已有的值
# hashMap.get(2);            // 返回 1
# hashMap.remove(2);         // 删除键为2的数据
# hashMap.get(2);            // 返回 -1 (未找到)
#
#
#
# 注意：
#
#
# 所有的值都在 [1, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希库。
#
#
#
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [None] * 10001

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
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

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = key // 100
        pair = self.data[hash_key]
        if pair is None:
            return -1
        elif isinstance(pair, tuple):
            if pair[0] == key:
                return pair[1]
        else:
            for i in pair:
                if i[0] == key:
                    return i[1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
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

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
if __name__ == "__main__":
    op = ["remove","put","remove","remove","get","remove","put","get"]
    arg = [[27],[65,65],[19],[0],[18],[3],[42,0],[19]]
    obj = MyHashMap()
    for op, arg in zip(op, arg):
        x = getattr(obj, op)(*arg)
        print(op, arg, obj.data[:10])
        print(repr(x))

