##包含min函数的栈##
##问题描述：定义栈的数据结构，请在该类型中实现一个能够
##得到栈中所含最小元素的min函数(时间复杂度应为O(1))。
##解题思路：
##首先题目要求时间复杂度为O(1)，这说明需要一个新的栈实时存储最小值，这样
##在调用min函数的时候可以马上给出最小值。然后需要注意的是如果出现push进去
##的值和当前最小值一样大的话，也要往min_num栈中push该值，这样在stack pop
##一个和当前最小值一样的数字的时候，min_num也pop一个之后仍然可以保证最小值
##不变。

class Solution:
	def __init__(self):
		#write code here
		self.stack = []
		self.min_num = []
    def push(self, node):
        # write code here
        if not self.min_num or node <= self.min_num[-1]:
        	self.min_num.append(node)
        self.stack.append(node)
    def pop(self):
        # write code here
        tnode = self.stack.pop()
        if tnode == self.min_num[-1]:
        	self.min_num.pop()
        
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_num[-1]


