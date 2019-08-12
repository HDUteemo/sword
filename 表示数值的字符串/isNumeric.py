##表示数值的字符串
##问题描述：实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
##但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是
##解题思路：
##1.e后面一定要接数字;
##2.不能同时存在两个e;
##3.第二次出现+-符号，则必须紧接在e之后;
##4.第一次出现+-符号，且不是在字符串开头，则也必须紧接在e之后;
##5.e后面不能接小数点，小数点不能出现两次；
##6.除了0-9, ., +, -, e, E都是不合法字符。

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        hasE = 0
        hasPoint = 0
        sign = 0

        length = len(s)
        for i in range(length):
        	if s[i] == 'e' or s[i] == 'E':
        		if hasE == 1:
        			return False
        		elif i == length - 1:
        			return False
        		hasE = 1
        	elif s[i] == '+' or s[i] == '-':
        		if i > 0:
        			if s[i - 1] != 'e' and s[i - 1] != 'E':
        				return False
        			else:
        				if i == length - 1:
        					return False
        		sign = 1
        	elif s[i] == '.':
        		if hasPoint == 1:
        			return False
        		elif hasE == 1:
        			return False
        		hasPoint = 1
        	else:
        		if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
        			return False

        return True

