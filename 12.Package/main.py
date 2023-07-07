# 主程式
import geometry.point # 匯入封包(Package)中的指定名稱模組
result = geometry.point.distance(3, 4) # 使用該模組的函式
print("距離", result)

import geometry.line as line # 一樣可使用別名的方式來對模組重新命名
result = line.slope(1, 1, 3, 3) # 當有使用別名後，就可以省略前面還要打封包名稱的部分
print("斜率", result)