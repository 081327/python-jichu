#多行输出
#将字符串 'Hello World!' 存储到变量str1中，再将字符串 'Hello Nowcoder!' 存储到变量str2中，再使用print语句将其打印出来（一行一个变量）。

import sys 
str1='Hello World!'
str2='Hello Nowcoder!'

#多个print()函数
print(str1)
print(str2)

#使用sep参数
print(str1,str2,sep=("\n")) #注意等于号不要丢，sep里面可以单引号，也可以双引号,对于字符串可以加单引号也可以双引号

#使用换行符
print(str1+'\n'+str2)


