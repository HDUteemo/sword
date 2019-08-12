##字符串的排列
##问题描述：
##输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
##则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
##解题思路：
##用递归实现n*(n-1)*(n-2) ... * 1情况
class Solution:
    def Permutation(self, ss):
        if len(ss) <=0:
            return []
        res = list()
        self.perm(ss,res,'')
        uniq = list(set(res))
        return sorted(uniq)
    def perm(self,ss,res,path):
        if ss=='':
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:],res,path+ss[i])
