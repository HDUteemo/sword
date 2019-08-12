##和为S的两个数字
##问题描述:输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
##如果有多对数字的和等于S，输出两个数的乘积最小的。
##解题思路:从小到大遍历，第一组和为S的数的乘积最小。

def FindNumbersWithSum(self, array, tsum):
    # write code here
    length = len(array)
    sum1 = 0
    sum2 = 0
    if length <= 1:
        return []
    for i in range(length):
        sum1 = array[i]
        if i == length -1:
            return []
        for j in range(i + 1, length):
            sum2 = array[j]
            if sum1 + sum2 == tsum:
                return [sum1, sum2]
        
    return []