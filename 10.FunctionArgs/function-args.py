# 參數的預設資料
def power(base, exp = 0):
    print(base ** exp)

power(3, 2)
power(4)

print("======使用參數的名稱對應======")
# 使用參數名稱對應（意思就是說可以不用按照函式指定的參數順序，只要名稱正確對應就可以）
def divide(n1, n2):
    print(n1 / n2)

divide(2, 4)
divide(n2 = 2, n1 = 4) # 仍可正常執行函式，因為參數名稱有正確對應到

print("======無限/不定 參數資料======")
# 無限/不定 參數資料
def avg(*nums):
    sum = 0
    for n in nums:
        sum += n
    print(sum / len(nums))

avg(3, 4)
avg(3, 5, 10)
avg(1, 4, -1, -8)