## 连续子数组的最大和##
##问题描述：
##例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
##给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
##解题思路：一种是暴力求解，计算速度慢。还有一种是动态规划。
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        sum_array = []
        for i in range(len(array)):
            for j in range(i, len(array)):
                sum_array.append(sum(array[i: j + 1]))
        return max(sum_array)

    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum = array[0]
        res = array[0]   
        for i in range(1, len(array)):
            max_sum = max(max_sum + array[i], array[i])
            res = max(max_sum, res);
        
        return res
        