# -*- coding:utf-8 -*-

# <SUBID:16416115,UPDATE:20220325>
# English:
# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
# Example 1:
# Input ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"] [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]] Output [null, null, null, 1, -1, null, 1, null, -1] Explanation MyHashMap myHashMap = new MyHashMap(); myHashMap.put(1, 1); // The map is now [[1,1]] myHashMap.put(2, 2); // The map is now [[1,1], [2,2]] myHashMap.get(1); // return 1, The map is now [[1,1], [2,2]] myHashMap.get(3); // return -1 (i.e., not found), The map is now [[1,1], [2,2]] myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value) myHashMap.get(2); // return 1, The map is now [[1,1], [2,1]] myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]] myHashMap.get(2); // return -1 (i.e., not found), The map is now [[1,1]]
# Constraints:
# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.
#
# 中文:
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
# 实现 MyHashMap 类：
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
# 示例：
# 输入： ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"] [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]] 输出： [null, null, null, 1, -1, null, 1, null, -1] 解释： MyHashMap myHashMap = new MyHashMap(); myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]] myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]] myHashMap.get(1); // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]] myHashMap.get(3); // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]] myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值） myHashMap.get(2); // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]] myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]] myHashMap.get(2); // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
# 提示：
# 0 <= key, value <= 106
# 最多调用 104 次 put、get 和 remove 方法


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

