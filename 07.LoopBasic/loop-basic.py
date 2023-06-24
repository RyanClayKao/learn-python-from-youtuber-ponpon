# while 迴圈
# 小範例：寫一個從 1開始累加到指定值的結果並印出
n = 1
sum = 0
while n <= 10:
    # print(n)
    sum += n    
    n += 1
print(sum)


# for 迴圈
print("=======for 迴圈=======")
# 依據列表的內容依序跑
for x in [3, 5, 1]:
    print(x)

# 依據字串，從字串的開頭字元到結束字元
for x in "Hello":
    print(x)

# range() 函數，可以指定數字範圍
# range(3) 代表範圍 0、1、2 (從零開始，到指定長度數量)
# range(3, 6) 代表範圍 3、4、5  (從指定開始值到結束值[不含結尾]的範圍)
print("======range(3)======")
for x in range(3):
    print(x)

print("======range(3,6)======")
for x in range(3, 6):
    print(x)

# 使用 for 迴圈一樣達到 1 到 10累加
sum = 0
for x in range(1, 11):
    sum += x
print(sum)