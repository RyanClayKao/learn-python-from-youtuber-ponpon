# 集合的運算
s1 = {3, 4, 5}
# 使用「in」來判斷某值是否在集合裡面
print(3 in s1) # result: True
print(10 in s1) # result: False
# 使用「not in」來判斷某值是否「不在」集合裡面
print(10 not in s1) # result: True

s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
# 交集運算「&」
print(s1 & s2) # result: {4, 5}
# 聯集運算「|」，重複的不會重複取
print(s1 | s2) # result: {3, 4, 5, 6, 7}
# 差集運算「-」，依據運算元左側的集合，減去運算元右邊集合相同的內容
print(s1 - s2) # result: {3}
# 反交集運算「^」，取不重疊的部分
print(s1 ^ s2) # result: {3, 6, 7}

# set() 函數：將傳入的字串拆解成集合，並且會去除多餘的重複
s = set("Hello")
print(s) # result: {'e', 'o', 'H', 'l'}  備註：由於集合是沒有順序性的，所以每次印出來的順序會不太一樣



print("======字典(Dictionary)======")
# 字典的運算
dic = {
    "apple": "蘋果",
    "bug": "蟲蟲",
}
print(dic) # result: {'apple': '蘋果', 'bug': '蟲蟲'}
print(dic["apple"]) # result: 蘋果

dic["apple"] = "小蘋果"
print(dic["apple"]) # result: 小蘋果

# 用「in」判斷 key是否存在
print("apple" in dic) # result: True
print("test" in dic) # result: False
# 用「not in」判斷 key是否「不」存在
print("test" not in dic) # result: True

# 用「del」刪除指定的 key value pair
del dic["apple"] # 刪除字典中 key 為 apple 的 key value pair
print(dic) # result: {'bug': '蟲蟲'}

# 從列表衍生出字典資料
dic = {x: x * 2 for x in [3, 4, 5]}
print(dic) # result: {3: 6, 4: 8, 5: 10}