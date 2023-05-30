#俱乐部的成员
#list=input().split(' ')
#name=input()
#print(name in list)
#法二
list=input().split(' ')
name=input()
for i in list:    #注意：善于使用for循环
    if(i==name):
     print(True)
    else:
      print(False) 
    
