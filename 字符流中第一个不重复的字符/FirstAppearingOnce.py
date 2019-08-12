##字符流中第一个不重复的字符
##问题描述:实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
##当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
##解题思路：利用字典的特性。字符作为字典的键名，出现次数作为键值。

# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.dict = {}
    def FirstAppearingOnce(self):
        # write code here
        length = len(self.s)
        for i in range(length):
            if self.dict[self.s[i]] == 1:
                return self.s[i]
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1