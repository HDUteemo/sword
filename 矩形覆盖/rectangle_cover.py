##矩形覆盖问题##
##问题描述：
##我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
##问题思路：
##第一次放的是2*1的小矩形的话，有f(n-1)情况；第一次放的是1*2的小矩形的话，有f(n-2)种情况；所以一共有f(n) = f(n - 1) + f(n - 2)种情况，这是斐波那契数列。
##python不适合用递归
def rectangle_cover(width):
	if width <= 0:
		return 0
	elif width == 1:
		return 1
	else:
		return rectangle_cover(width - 1) + rectangle_cover(width - 2)
##用数组模拟斐波那契数列，速度更快
def rectangle_cover2(width):

	res = [0, 1, 2]
	if width <= 0:
		return res[0]
	elif width == 1:
		return res[1]
	elif width == 2:
		return res[2]
	else:
		for i in range(2, width):
			temp = res[-1] + res[-2]
			res.append(temp)
		return res[-1]
if __name__ == '__main__':
	width = int(input())
	case_number = rectangle_cover2(width)
	print('方案总数: ', case_number)