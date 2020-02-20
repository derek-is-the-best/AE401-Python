import random as rm
d={}
while True:
    a=int(input("請輸入功能 1-建立字彙表 2-列出全部單字 3-英翻中 4-中翻英 5-測驗學習成果 6-結束:"))
    if a==1:
        while True:
            english=input("請輸入英文(輸入0結束):")
            if english=="0":
                break
            chinese=input("請輸入中文:")
            d[english] = chinese
    elif a==2:
        for key,value in d. items():
            print(key,value)
    elif a==3:
        english1=input("請輸入英文:")
        if english1 in d: 
            print(english1,"的中文為",d[english1]) 
        else:
            print("查無此字")
    elif a==4:
        chinese1=input("請輸入中文:")
        temp=0
        for key,value in d.items():
             if chinese1 == value: 
                 print(value,"的英文為",key)
                 temp=1
        if temp==0:
            print("查無此字")
                
    elif a==5:
        key,value = rm.choice(list(d.items()))
        print(key)
        dictionary=input("請回答上面那個字的意思:")
        if dictionary==value:
            print("還不錯嘛")
        else:
            print("要認真讀書喔")
    else:
        print("謝謝您的使用！！！")
        break
    
        

