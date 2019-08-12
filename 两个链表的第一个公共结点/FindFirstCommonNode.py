##两个链表的第一个公共结点
##输入两个链表，找出它们的第一个公共结点。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 == None or pHead2 == None:
            return None
        temp1 = pHead1
        temp2 = pHead2
        
        while(temp1 != None):
            temp2 = pHead2
            while(temp2 != None):
                if temp1 == temp2:
                    return temp1
                temp2 = temp2.next
            if temp1.next != None:
                temp1 = temp1.next
            else:
                return None