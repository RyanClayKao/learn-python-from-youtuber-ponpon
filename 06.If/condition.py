# 判斷式

# 備註： python 3.6暫不支援 switch，但往後會不會支援，不確定

# input函數可以請使用者輸入，輸入後會取得字串形式的輸入值
x = input("請輸入數字: ") 
x = int(x) # 將字串轉型為數字型態
if x > 200:
    print("大於 200")
elif x > 100:
    print("大於 100, 小於等於 200")
else:
    print("小於等於 100")

# 小練習
print("======小練習======")
# 四則運算
n1 = int(input("請輸入數字一: "))
n2 = int(input("請輸入數字二: "))
op = input("請輸入一種運算元(+, -, *, /): ")
if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)
else:
    print("您輸入了錯誤的運算元")