scoreList = []
for i in range(5):
    score=int(input("輸入五個數字"))
    scoreList.append(score)

print(max(scoreList))
print(min(scoreList))
print(sorted(scoreList))
print(len(scoreList))
print(sum(scoreList))