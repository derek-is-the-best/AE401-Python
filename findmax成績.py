num = int(input("班上總共多少人:"))#輸入人數

scorelist = []
highList = []
lowList = []

for i in range(0,num,1):
    templist = []
    name = input("叫什麼名字:")#輸入名字
    score = int(input("他的分數:"))#輸入分數
    templist.append(name)#弄到小框框
    templist.append(score)#弄到小框框
    scorelist.append(templist)#弄到大框框


print(sorted(scorelist, key = lambda x:x[1]))
print("最高的是",max(scorelist, key = lambda x:x[1]))
print("最低的是",min(scorelist, key = lambda x:x[1]))