#二进制位运算
list=input().split(' ')
a=int(list[0])
b=int(list[1])
print(int(bin(a&b),2))
print(int(bin(a|b),2))


