##问题描述:
##一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法

def jump2(number):
	if number == 0:
		return -1
	else:
		return pow(2, number - 1)


if __name__ == '__main__':
	number = int(input())
	case_num = jump2(number)
	print('方案总数： ', case_num)