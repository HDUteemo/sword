##复杂链表的复制
##问题描述：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
##返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）。
##解题思路：
##第一步：不管random的指向，先简单复制链表； 第二步：遍历原链表，将random指向的结点的位置记录下来；
##第三步：给新的链表添加random信息。

# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
def Clone(self, pHead):
	new_temp = RandomListNode(None)
	temp = RandomListNode(None)
	random_Node_Index = []

	temp = pHead
	new_head = new_temp

	while temp != None:
		p_Node = RandomListNode(None)
		p_Node.label = temp.label
		new_temp.next = p_Node
		temp = temp.next
		new_temp = new_temp.next
	new_head = new_head.next

	
	temp = pHead
	while temp != None:
		ptemp = pHead
		count = 0
		while ptemp!= None:
			if temp.random == None:
				random_Node_Index.append(None)
				break
			elif temp.random == ptemp:
				random_Node_Index.append(count)
			else:
				count += 1
			ptemp = ptemp.next
		temp = temp.next

	new_temp = new_head

	for i in range(len(random_Node_Index)):
		pnew_temp = new_head
		if random_Node_Index[i] == None:
			new_temp.random = None
		else:
			for j in range(random_Node_Index[i]):
				pnew_temp = pnew_temp.next
			new_temp.random = pnew_temp
		new_temp = new_temp.next

	return new_head


