# 數字運算
x = 1
y = 2
# 加(+)、減(-)
print("======加、減======")
print(x + y) # result: 3
print(x - y) # result: -1

# 乘(*)、除 (小數除法[/]、整數除法[//])、取餘數(%)
print("======乘、除(小數除法、整數除法)、取餘數======")
print(x * y) # result: 2
print(x / y) # result: 0.5
print(x // y) # result: 0
print(4%3) # result: 1

# 指數(**)、開根號(**0.5)
print("======指數、開根號======")
print(2**3) # result: 8
print(2**0.5) # result: 1.4142135623730951
print(144**0.5) # result: 12.0

# 數字型態的變數運算
print("======數字型態的變數運算======")
z = 1 + 1
print(z) # result: 2
z = x + y
print(z) # result: 3
z = z - 1 # 3 - 1 = 2
print(z) # result: 2

# 數字型態的變數運算簡寫方式
print("======數字型態的變數運算簡寫方式======")
z = 3
z = z + 1
print(z) # 3 + 1 = 4,  result: 4
# 簡寫方式，例如 「+=」、「-=」、「*=」、「/=」
z += 1
print(z) # 4 + 1 = 5, result: 5

# ===============
# 字串運算
# 可以用雙引號(")或是單引號(')來表示字串都可以
print("=======字串運算======")
print("* 基礎使用: ")
s1 = "Hello"
s2 = "World"
print(s1)
print(s2)

# 跳脫字元(\)
print("=======跳脫字元======")
s = "Hell\"o" # result: Hell"o
print(s)

# 字串串接，使用「+」或是空格
print("=======字串串接======")
s = "Hello" + "Hello"
print(s) # result: HelloHello
s = "Hello" "Hello"
print(s) # result: HelloHello

# 換行字元，使用「\n」
print("=======換行字元======")
print("Hello\nWorld")

# 多行字串，使用「"""」或「'''」來包住要表示的字串
# 備註：無法透過程式碼排版呈現想要的斷行，如果用了像是 tab或是空格的方式來排版，那些都會被顯示出來
print("=======多行字串======")
s = """Hello
World"""
print(s)

# 使用「*」達到重複出現字串
print("=======使用「*」達到重複出現字串======")
s = "Hello" * 3
print(s) # result: HelloHelloHello

# 可以像是數學運算一樣，先乘除後加減（先用「*」讓字串重複出現，再字串串接
s = "Hello" * 3 + "World" 
print(s) # result: HelloHelloHelloWorld

# 字串的字元索引(index)，index從 0 開始
# 使用「[index值]」、取指定索引範圍字串(使用「:」)，包含開頭而不包含結尾！
print("=======字串的字元索引、取範圍字串======")
s = "Hello"
print(s[1]) # result: e

# 特別注意!此用法包含開頭，不包含結尾
# 像是 javascript 陣列的 slice()，含開頭不含結尾的用法
print(s[1:4]) # result: ell
# 特別用法 1: 不給結尾，等同於從指定開始的index取到結尾
print(s[1:]) # result: ello
# 特別用法 2: 不給開頭，等同於從頭取到指定index結尾
print(s[:4]) # result: Hell
