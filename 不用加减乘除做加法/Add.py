##不用加减乘除做加法
##问题描述:写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
##解题思路：两个数的二进制异或得到的数是不算进位的加法，原理可以参考非进位加法器。两个数的相与得到的是进位，
##但是要把得到的数左移一位 比如 010 & 110 = 010 左移一位为0100，说明第二位进位给第三位。要循环进行两个操作
##知道不再有进位为止。

def Add(num1, num2):
        # write code here
        sum_no_carry = num1
        carry = num2
        while(carry != 0):
            temp = sum_no_carry ^ carry
            carry = (sum_no_carry & carry) << 1
            sum_no_carry = temp
        return sum_no_carry


if __name__ == '__main__':
	result = Add(51232123123123,701232134234234234234)
	print('result: ', result)