# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m = len(array)
        n = len(array[0][:])
        # print('m:', m)
        # print('n:', n)
        for i in range(m):
            for j in range(n):
                if target > array[i][j]:
                    if i == m - 1 and j == n - 1:
                        return False
                    else:
                        continue
                elif target == array[i][j]:
                    return True
                else:
                    if i == m - 1 and j == n - 1:
                        return False
                    else:
                        break

if __name__ == '__main__':
    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    s = Solution()
    re = s.Find(10, array)
    print('reuslts:', re)