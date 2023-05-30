#牛牛的绩点
gidian_score=0.0
total_score=0
while True:
 score=float(input('请输入一个成绩：'))
 dengji=input('请输入一个等级：')
 print(score)
 print(dengji)
 if dengji=='False':
    break
 elif dengji=='A':
   gidian_score+=4.0*score
 elif dengji=='B':
   gidian_score+=3.0*score
 elif dengji=='C':
   gidian_score+=2.0*score
 elif dengji=='D':
   gidian_score+=1.0*score
 else:
   gidian_score+=0.0*score
total_score+=score
print('{:.2f}'.format(float(gidian_score/total_score)))

#法二：
#dict1 = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0}   #用字典的形式
#list1 = [] # 等级 * 学分 = 总成绩
#list2 = [] # 学分数
#while True:
 #   grade = input()
  #  if grade == 'False':
   #     break   #break用于for或者while循环
   # else:
    #    score = int(input())
     #   list1.append(dict1[grade] * score)
      #  list2.append(score)
#print('{:.2f}'.format(sum(list1) / sum(list2)))   #sum函数对序列进行求和计算

   