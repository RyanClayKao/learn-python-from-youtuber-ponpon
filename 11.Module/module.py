# 「載入內建的 sys 模組並取得資訊」
# import sys as system  # 可用 as 接上要使用的暱稱
# print(sys.platform) # 印出作業系統
# print(sys.maxsize) # 印出整數最大值
# print(sys.path) # 印出搜尋模組的路徑



# 「建立 geometry 模組，載入並使用」
# import geometry  # 當該模組檔案在同一資料夾內時，可以直接這樣使用
# result = geometry.distance(1, 1, 5, 5)
# print(result)
# result = geometry.slope(1, 2, 5, 6)
# print(result)

# 「調整搜尋模組的路徑」
import sys
sys.path.append("modules") # 加入當前專案資料夾下的 module資料夾到搜尋模組的路徑中；也可用絕對或相對路徑表示
print(sys.path) # 印出模組的搜尋路徑
print("------------")
import geometry
print(geometry.distance(1, 1, 5, 5))