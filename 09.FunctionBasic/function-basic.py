# 定義函式
# 備註：沒有寫 return 時，那就沒有回傳東西，
#      但如果被呼叫的函式被塞給某一變數，並將變數或函式直接印出，那會得到 None
def multiply(n1, n2):
    print(n1 * n2)

# 呼叫函式
multiply(3, 4)
multiply(10, 8)

value = multiply(3, 4)
print(multiply(3,4))
print("value: ", value) # result: None，因為函式中並沒有定義 return 的東西，所以預設給 None

# ====== 當有定義函式回傳值時，依據 return 後的程式回傳最終結果
def multiplyDirectReturn(n1, n2):
    return n1 * n2

value = multiplyDirectReturn(3, 4)
print("value: ", value)


# 函式可以用來做程式的包裝：同樣的邏輯可以重複利用
def calculate(maxNum):
    sum = 0
    for n in range(1, maxNum + 1):
        sum += n
    print(sum)

calculate(10)
calculate(20)