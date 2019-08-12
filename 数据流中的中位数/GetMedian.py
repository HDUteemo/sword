##数据流中的中位数
##问题描述：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
##如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用
##GetMedian()方法获取当前读取数据的中位数。
##解题思路：边插入数据，边排序，然后取中位数。注意：牛客网题目出现问题，GetMedian莫名其妙需要两个参数。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.seq = []
    def Insert(self, num):
        # write code here
        self.seq.append(num)
        self.seq.sort()
    def GetMedian(self, dog):
        # write code here
        length = len(self.seq)
        if length == 0:
            return None
        if length % 2 == 0:
            median = float((self.seq[length/2 - 1] + self.seq[length/2]))/2
        else:
            median = float(self.seq[(length - 1)/2])
        return median
