##顺时针打印矩阵##
##问题描述：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
##例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
##则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
##解题思路:
##一个循环分四步，第一步将第一行全部遍历，第二步将最后一列剩余的遍历，第三步将最后一行剩余的
##全部遍历，第四步将第一列剩余的全部遍历。


def printMatrix(matrix):
	row = len(matrix)
	col = len(matrix[0])
	if row <= 1 and col <= 1:
		return [matrix[0][0]]
	all_list = []
	start = 0

	end_row = row - 1 - start
	end_col = col - 1 - start
	while(start <= end_row and start <= end_col):
		
		for i in range(start, end_col + 1):
			all_list.append(matrix[start][i])
		for j in range(start, end_row):
			all_list.append(matrix[j + 1][end_col])
		if end_row > start:
			for k in range(start, end_col):
				all_list.append(matrix[end_row][end_col - 1 - (k - start)])
		if end_col > start:
			for l in range(start + 1, end_row):
				all_list.append(matrix[end_row - (l - start)][start])
		start += 1
		end_row = row - 1 - start
		end_col = col - 1 - start
	return all_list


if __name__ == '__main__':
	# matrix = [[1, 2, 3, 4],
	# 		  [5, 6, 7, 8],
	# 		  [9, 10, 11, 12],
	# 		  [13, 14, 15, 16]]
	# matrix = [[1,2,3,4,5]]
	matrix = [[1]]
	all_list = printMatrix(matrix)
	print('results: ', all_list)