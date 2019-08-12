##	调整数组顺序使奇数位于偶数前面
##问题描述：
##输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
##所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。\
##解题思路：新建三个数组new_array，odd_array，even_array，odd_array存按顺序的所有奇数，even_array存按顺序的所有偶数，new_array存奇数+偶数

def odd_even(array):
	new_array = [0 for x in array]
	odd_array = []
	even_array = []

	if len(array) == 0:
		return new_array
	for i in range(len(array)):
		if array[i] % 2 == 1:
			odd_array.append(array[i])
		else:
			even_array.append(array[i])
	new_array[ : len(odd_array)] = odd_array
	new_array[len(odd_array) : ] = even_array

	return new_array






if __name__ == '__main__':
	array = [int(x) for x in input().split()]
	new_array = odd_even(array)
	print('新数组： ', new_array)