apple=0
price=0
applelist = []
applelist2=[]
apple4=0
while True:
    a=int(input("請選擇一個功能 1-設定 2-進貨 3-出貨 4-營業額 5-庫存 6-結束 7-老闆資產 8-輸入老闆資產"))#問要哪個功能
    if a==1:
       apple=int(input("總共有幾顆蘋果？"))#問總共幾顆蘋果
       price=int(input("一顆蘋果多少錢？"))#問一顆蘋果要幾元
       print("蘋果庫存有",apple,"顆")#把庫存印出
       print("一顆蘋果",price,"元")#把價格印出
    elif a==2:
        apple1=int(input("總共進貨幾顆？"))#問進貨幾顆
        print('加了',apple1,"顆蘋果")#印出進貨幾顆
        applelist2.append(apple1)#把進貨加到清單中
        apple+=apple1#計算庫存
        print("蘋果庫存有",apple,"顆")#印出庫存
        price2=price*apple1#計算花多少元
        print("總共花了",price2,"元")#印出花多少元
        print("每次的進貨數量",applelist2)#印出每次進貨多少
    elif a==3:
        apple2=int(input("總共出貨幾顆？"))#問出貨幾顆
        print('減了',apple2,"顆蘋果")#印出出貨幾顆
        applelist.append(apple2)#把出貨加到清單中
        apple-=apple2#計算庫存
        print("蘋果庫存有",apple,"顆")#印出庫存
        price1=apple2*price#計算賺多少錢
        print("總共賺了",price1,"元")#印出賺多少錢
        print("每次的出貨數量",applelist)#印出每次出貨多少
    elif a==4:
        apple3=sum(applelist)*price#算營業額
        print("今天的營業額是",apple3,"元")#印出營業額
    elif a==5:
        print("蘋果庫存有",apple,"顆")#印出庫存
    elif a==6:
        print("謝謝你的使用！！！")
        break
    elif a==7:
        apple5=(sum(applelist)*price)-(sum(applelist2)*price)
        apple4=apple5+apple4
        print("老闆身上有",apple4,"元")
    else:
        apple4=int(input("老闆身上有幾元？"))
    