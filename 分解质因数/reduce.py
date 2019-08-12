def num(n):
    print('{}='.format(n),end=''),
    if not isinstance(n,int) or n<=0:
        print('请输入正确的数字！')
        exit(0)
  
    elif n ==1:
        print('{}'.format(n))
    else:
        while n != 1: ###
            for i in range(2, n+1):
                if n % i == 0:
                    n = int(n/i)  ## n/=i 出来float
                    if n==1:
                        print (i)
                    else:
                        print('{}*'.format(i),end='')
                    break

if __name__ == '__main__':
    num(40)