
import time,datetime
def get_week_day(date):
    week_day_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期天',
    }
    day = date.weekday()
    return week_day_dict[day]

from datetime import datetime

now = datetime.now()      # 現在時間
week=get_week_day(now)
print("現在:",week)
current_time = now.strftime("%Y-%m-%d  %H:%M:%S")   # 印出時間的格式
print("現在時間 =", current_time)

txt = "Hello, welcome to my world welcome."
x = txt.find("welcome")
x = txt.replace("welcome","apple")
print(x)

