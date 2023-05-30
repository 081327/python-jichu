#密码游戏
a=int(input('请输入一个整数：'))   
#4位整数取每位数值的方法
first=a//1000
second=(a//100)%10
third=(a//10)%10
fourth=a%10
arr=[first,second,third,fourth]
for i in range(len(arr)):    #冒号记得不要丢，len()记得不要丢
    arr[i]=(arr[i]+3)%9     
    arr[0],arr[2]=arr[2],arr[0]   #交换
    arr[1],arr[3]=arr[3],arr[1]
    print(arr[0],arr[1],arr[2],arr[3],sep='')
     
