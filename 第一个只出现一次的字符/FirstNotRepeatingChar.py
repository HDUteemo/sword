##第一个只出现一次的字符
##问题描述：在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
##并返回它的位置, 如果没有则返回 -1（需要区分大小写）
##解题思路：建立三个数组,index存储字符的下标，num存储字符出现的次数，strs存储已经出现的字符。
##遍历整个字符串，当前字符如果不在strs中，那么将该字符加入strs，并且存储该字符的index,以及初
##始化字符出现的次数为1；但是如果该字符已经在strs中，那么就找到该字符的位置，num += 1。遍历完毕
##后，从num数组中找到值为1的第一个下标，然后返回该字符第一次出现的位置。


# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) == 0:
            return -1
        index = []
        strs = []
        num = []
        for i in range(len(s)):
            if s[i] not in strs:
                strs.append(s[i])
                num.append(1)
                index.append(i)
            else:
                loc = strs.index(s[i])
                num[loc] += 1
        for i in range(len(num)):
            if num[i] == 1:
                return index[i]
        return -1