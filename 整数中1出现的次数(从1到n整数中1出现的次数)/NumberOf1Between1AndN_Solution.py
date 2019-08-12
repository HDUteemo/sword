##整数中1出现的次数（从1到n整数中1出现的次数）
##问题描述：从1 到 n 中1出现的次数
##解题思路： 分别统计个，十，百...各位的出现次数。
def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        num = n
        array = []
        result = 0
        count = 0
        mod = []
        while num > 0:
            if num%10 > 1:
                num = num/10
                array.append(num + 1)
                mod.append(0)
            elif num%10 == 1:
                num = num/10
                array.append(num)
                mod.append(n%(pow(10,count)) + 1)
            else:
                num = num/10
                array.append(num)
                mod.append(0)
            count += 1
        for i in range(len(array)):
            result += array[i] * pow(10, i) + mod[i]
        return result
