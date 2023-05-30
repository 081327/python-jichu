#格式化输出
#牛牛、牛妹和牛可乐都是Nowcoder的用户，某天Nowcoder的管理员由于某种错误的操作导致他们的用户名的左右两边增加了一些多余的空白符（如空格或'\t'等），
#现在给定他们三个当中的某一个名字name，请输出name去掉两边的空白符后的原本的内容。
#python中去掉空格的方法有以下几种

#1.使用lstrip()函数去掉左边空格

#2.使用rstrip()函数去掉右边空格

#3.使用strip()函数去掉左右两边空格

#4.使用replace()函数去掉所有空格
 #a_new = a.replace(" ", "")
  #  print (a_new)
a=input()
print(a.lstrip())
