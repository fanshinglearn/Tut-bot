import datetime

# 獲取當前時間
a = datetime.datetime.now()
now_time = datetime.datetime.now().strftime('%H%M')

# 日期時間轉換
b = datetime.datetime(2019, 10, 10, 10, 10, 10)
print(now_time)