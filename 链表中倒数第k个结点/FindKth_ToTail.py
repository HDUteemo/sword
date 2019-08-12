##链表中倒数第k个结点
##问题描述：输入一个链表，输出该链表中倒数第k个结点。
##思路：先遍历链表，知道整个链表的长度，然后开始从头找到倒数k的结点
##注意：有些题目的头结点可能是空，也有可能是非空的。
def FindKth_ToTail(head, k):
	length = 0
	pHead = head
	if pHead == None or pHead.next == None:
		return 
	while(pHead != None):
		length += 1
		pHead = pHead.next
	if length > k or k <= 0:
		return
	tNode = head
	for i in range(length - k):
		tNode = tNode.next
	return tNode