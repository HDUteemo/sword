# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        if listNode is None:
            return result
        while listNode.next:
            result.append(listNode.val)
            listNode = listNode.next
        result.append(listNode.val)

        return result[ : : -1]

'''
python用结构体来模仿链表，self.val 是该结构体的值， self.next指向下一个结构体
result[::-1]为list倒序输出
result[start:end:size]
'''

