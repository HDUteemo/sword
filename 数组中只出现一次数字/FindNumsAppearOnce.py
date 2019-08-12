##数组中只出现一次的数字
##问题描述：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        seq = sorted(array)
        length = len(seq)
        
        temp = seq[0]
        count = 1
        result = []
        for i in range(1, length):
            if seq[i] != temp:
                if count == 1:
                    result.append(temp)
                temp = seq[i]
                count = 1
            else:
                count += 1
            if i == length - 1 and count == 1:
                result.append(temp)
        
        return result

if __name__ == '__main__':
    s = Solution()
    array = [2,4,3,6,3,2,5,5]
    result = s.FindNumsAppearOnce(array)
    print(result)