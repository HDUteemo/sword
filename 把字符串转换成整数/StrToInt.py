##把字符串转换成整数
##问题描述：将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
##要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
##解题思路：字符串第一位可能是符号位，需要先进行判断。随后每一位字符都和'0'ASCII码进行比较，在0~9范围内认为
##是合理数字，否则直接返回0。

class Solution:
    def StrToInt(self, s):
        # write code here
        length = len(s)
        flag = 1
        num = 0
        for i in range(length):
            if i == 0:
                if s[i] == '+':
                    flag = 1
                    continue
                elif s[i] == '-':
                    flag = -1
                    continue
            interval = ord(s[i]) - ord('0')
            if interval >= 0 and interval <= 9:
                num = num * 10 + interval
            else:
                return 0
            
        return num * flag