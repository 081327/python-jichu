#菜品的价格
#dish_list=['pizza', 'rice', 'yogurt']
#dish=input('请输入一个菜品：')
#print(dish)
#if dish in dish_list:
 #   if dish=='pizza':   #注意右边的单引号不要忘了，因为左边是字符串的形式，右边也得是字符串的形式，所以必须加上单引号
  #      print(10)
   # elif dish=='rice':
    #    print(2)
    #elif dish=='yogurt':
     #   print(5)
    #else:
     #print(8)
#else:
 #  print(8)



#法二：字典
dict={'pizza':10,'rice':2,'yogurt':5}
x=input('请输入一个字符串：')
print(x)
if x in dict:
   print(dict[x])   #注意：dict[]里面的x不用再加单引号，因为x已经是字符串形式，如果不是字符串形式则要加单引号，还能用dict.get(x)的形式，里面的x与前面所说的一样，必须得是字符串形式
   
else:
   print(8)
