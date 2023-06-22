# 有序可變動列表 List
grades = [12, 60, 15, 70, 90]
print(grades) # 印出整個列表
print(grades[3]) # 使用 index取得該索引位置的資料
# 取得指定區間內的資料，包含開始的位置，但不包含結尾位置的資料
# (概念像 javascript 陣列的 slice)
print(grades[1:4]) # result: [60, 15, 70]

grades[1:4] = [] # 依據指定的索引區間刪除資料
print(grades) # result: [12, 90]

grades[0] = 55 # 修改指定索引位置的資料值
print(grades)

# 列表串接
grades = grades + [12, 33]
print(grades)

# 取得列表長度，使用 len() 函數
length = len(grades)
print(length)

# 巢狀列表
data = [[1, 2, 3,], [4, 5, 6]]
print(data) # result: [[1, 2, 3,], [4, 5, 6]]
print(data[0]) # result: [1, 2, 3]
print(data[0][0]) # result: 1

data[0][0:2] = [5, 5, 5] # 把指定位置及區間的資料替換掉
print(data[0]) # result: [5, 5, 5, 3]
print(data) # result: [[5, 5, 5, 3], [4, 5, 6]]

# ===============
print("========Tuple=========")
# 有序不可變動列表 Tuple
data = (3, 4, 5)
print(data[0]) # result: 3
print(data[0:2]) # result: (3, 4)

data[0] = 1 # 會噴錯，因為 tuple 不允許更動資料
print(data)