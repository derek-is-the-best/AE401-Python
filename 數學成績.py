num = int(input("班上總共多少人:"))
scorelist = []
highest = 0
highestPerson = 0
lowestPerson=0
lowest = 100
for i in range(int(num)):
    name = input("班上人的名字")
    score = int(input("同學是幾分"))
    scorelist.append(score)
    if highest<score:
        highest=score
        highestPerson=name
    if lowest>score:
        lowest=score
        lowestPerson=name
    average = sum(scorelist)/int(num)

print("最高分是",highest)       
print("最低分是",lowest)
print("最高分的人",highestPerson)
print("最低分的人",lowestPerson)   
print("平均是",average)    


    
   