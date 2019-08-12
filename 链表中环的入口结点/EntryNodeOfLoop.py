##链表中环的入口结点
##问题描述：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
##解题思路：
##1.直接将每个结点存入列表中，在循环过程中第一次出现结点已经在列表中出现的情况就说明该结点是环入口结点；若遍历完都没有出现，
##说明该链表不存在环，返回None。
##2.用断链表的方法(不可取，会将链表的结构破坏，失去意义)。用两个指针，一个指着前面，一个指着后一个，然后每次讲前面指针所指的
##结点.next = flag， flag是新定义的一个结点，当出现后指针所指的结点.next == flag的时候，说明该结点是环入口，但是如果.next=null,
##说明无环。
##3.用快慢指针的方式来得到环入口结点。慢指针slow一次步长1，快指针quick一次步长2。若存在环，快慢指针会出现一次重叠slow = quick;
##此时假设慢指针走了n步，那么快指针走了2n步，两者重叠说明快指针比慢指针多走了一圈，那么说明一圈步长为n，有n个结点。此时让快指针指向
##头指针，步长改为1，当两者再次重叠的时候就是环入口结点。因为假设总步长为n+a，环步长为n,那么从头开始走a步会达到环入口结点，同理走了n
##步后再走a步也会走到环入口结点。


##方法1：
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        #遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
        tempList = []
        p = pHead
        while p:
            if p in tempList:
                return p
            else:
                tempList.append(p)
            p = p.next
        return None

##方法2：

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return None
        pre = pHead
        front = pHead.next
        flag = ListNode(0)
        while(front != None and front != flag):
            pre.next = flag
            pre = front
            front = front.next
        return front if front == None else pre



##方法3：
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None and pHead.next == None:
        	return None

        quick = pHead
        slow = pHead
 		
 		while quick != None and quick.next != None:
 			slow = slow.next
 			quick = quick.next
 			quick = quick.next
 			if quick == None:
 				return None
 			elif quick == slow:
 				quick = pHead
 				while quick != slow:
 					slow = slow.next
 					quick = quick.next
 				return slow