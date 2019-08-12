##丑数
##问题描述：
##把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
##习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数
##解题思路：将丑数存在数组res中，初始都指向数组头，因为所有丑数必定是之前某丑数的2,3,5倍。res是从小到大排列的
##min(res[t2] * 2,res[t3] * 3,res[t5] * 5)找到下一个数，然后比较min和res[t2] * 2，res[t3] * 3，res[t5] * 5
##相等的话移动指针(想象成指针，实际是数组下标)

##算法超时
# class Solution:
#     def GetUglyNumber_Solution(self, index):
#         # write code here
#         if index == 1:
#             return 1
#         count = 1
#         num = 1
#         while count < index:
#             num += 1
#             temp = num
#             while temp > 1:
#                 if temp % 2 == 0:
#                     temp /= 2
#                 elif temp % 3 == 0:
#                     temp /= 3
#                 elif temp % 5 == 0:
#                     temp /= 5
#                 else:
#                     break
#                 if temp == 1:
#                     count += 1
#         return num
## 优化算法

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        if index == 1:
            return 1
        res = [1]    
        t2 = t3 = t5 = 0
        count = 1
        for i in range(1,index):
            res.append(min(res[t2] * 2,res[t3] * 3,res[t5] * 5))
            if res[i] == res[t2] * 2:
                t2 += 1
            if res[i] == res[t3] * 3:
                t3 += 1
            if res[i] == res[t5] * 5:
                t5 += 1
        return res[index - 1]

if __name__ == '__main__':
    s = Solution()
    num = s.GetUglyNumber_Solution(7)
    print(num)