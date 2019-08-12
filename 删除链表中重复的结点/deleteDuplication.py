##删除链表中重复的结点
##问题描述:
##在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
##例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
##解题思路：
##1. 首先添加一个头节点，以方便碰到第一个，第二个节点就相同的情况
##2.设置 temp，temp_next指针，标志flag，来找到必定不重复的结点。


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return None
        elif pHead.next == None:
            return pHead
        flag = 0
        new_head = None
        temp = pHead
        temp_next = pHead.next
        pnew = new_head
        
        while temp_next != None:
            if temp.val != temp_next.val and flag == 0:
                if new_head == None:
                    new_head = temp
                    pnew = new_head
                    temp = temp.next
                    temp_next = temp_next.next
                    pnew.next = None
                else:
                    pnew.next = temp
                    pnew = pnew.next
                    temp = temp.next
                    temp_next = temp_next.next
                    pnew.next = None
                    
            elif temp.val != temp_next.val and flag == 1:
                temp = temp.next
                temp_next = temp_next.next
                flag = 0
            elif temp.val == temp_next.val:
                temp = temp.next
                temp_next = temp_next.next
                flag = 1
        if flag == 0 and temp != None:
            if new_head == None:
                new_head = temp
            else:
                pnew.next = temp

        return new_head



##递归方法：
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        head1 = pHead.next
        if head1.val != pHead.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            while pHead.val == head1.val and head1.next is not None:
                head1 = head1.next
            if head1.val != pHead.val:
                pHead = self.deleteDuplication(head1)
            else:
                return None
        return pHead