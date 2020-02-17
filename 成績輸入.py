num = int(input("班上總共多少人:"))#輸入人數

scorelist = []
highest = 0
highestPerson = 0
lowestPerson=0
lowest = 100
for i in range(1,num*2,2):
    name=input("叫什麼名字:")#輸入名字
    score = int(input("他的分數:"))#輸入分數
    scorelist.append(name)
    scorelist.append(score)

total=0
for i in range(1,num*2,2):
    total=total+scorelist[i]
average=total/int(num)#算平均
    
for i in range(1,num*2,2):
    if highest<scorelist[i]:
        highest=scorelist[i]#最高分
        highestPerson=scorelist[i-1]#最高分的人
    if lowest>scorelist[i]:
        lowest=scorelist[i]#最低分
        lowestPerson=scorelist[i-1]#最低分的人

print(scorelist)
print("最高分是",highest)       
print("最高分的人",highestPerson)
print("最低分是",lowest)
print("最低分的人",lowestPerson)   
print("平均是",average)
   

