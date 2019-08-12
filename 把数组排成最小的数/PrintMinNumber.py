##把数组排成最小的数
##问题描述：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
##例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
##解题思路：先将整型数组转换成String数组，然后将String数组排序，最后将排好序的字符串数组拼接出来。关键就是制定排序规则。
##排序规则如下：
##若ab > ba 则 a > b，
## * 若ab < ba 则 a < b，
## * 若ab = ba 则 a = b；
## * 解释说明：
## * 比如 "3" < "31"但是 "331" > "313"，所以要将二者拼接起来进行比较

##自己的思路，以{3，32，321}为例，3变成333333,32变成323232,321变成321321，然后比较，小的放在前面，但是
##该思路对于{1, 11, 111}这种情况无法通过，所以对于1 变成111111+1,11变成111111+2,111变成111111+3。

# class Solution:
#     def PrintMinNumber(self, numbers):
#         # write code here
#         num_array = numbers 
#         str_array = []
#         temp_str_array = []
#         temp_num_array = []
#         num_len = 0
#         str_len = 0
#         result = ''
#         for i in range(len(num_array)):
#             str_array.append(str(num_array[i]))
#             num_len += len(str_array[i])
#         for i in range(len(str_array)):
#             str_len = len(str_array[i])
#             temp_str_array.append(str_array[i])
#             while str_len <= num_len - len(str_array[i]):
#                 temp_str_array[i] += str_array[i]
#                 str_len += len(str_array[i])
#             temp_str_array[i] += str_array[i][:num_len - str_len] + i
#             temp_num_array.append(int(temp_str_array[i]))
#         sorted_array = sorted(temp_num_array)
#         print('sorted: ', sorted_array)
#         for i in range(len(temp_num_array)):
#             result += str_array[temp_num_array.index(sorted_array[i])]
#         num = int(result)
#         return num

##最好解题思路,只有在python2x可以这么写strs.sort(self.str_cmp)
class Solution:
    def str_cmp(self,s1,s2):
        sa = s1+s2
        sb = s2+s1
        if sa > sb:
            return 1
        elif sa == sb:
            return 0
        else:
            return -1

    def PrintMinNumber(self, numbers):
        # write code here
        strs = [] 
        if not numbers:
            return ''
        for i in range(len(numbers)):
            strs.append(str(numbers[i]))
        strs.sort(self.str_cmp)
        return ''.join(strs)


if __name__ == '__main__':
    s = Solution()
    array = [3,32,321]
    num = s.PrintMinNumber(array)
    print(num)