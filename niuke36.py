#谁的数字大
a=int(input('请输入第一个数：'))
b=int(input('请输入第二个数：'))
print(a,b,sep=' ')
if(a>b):
 print(True)
else:
  print(False) 
if(a<b):
 print(True)
else:
  print(False)   

  #方法2
#x,y = input().split()
#print(int(x) > int(y))
#print(int(x) < int(y))

#方法3
#x,y = input().split()
#num = []
#num.append(x)
#num.append(y)
#for i in num:
 #   i = int(i)
#print(x>y)
#print(x<y)