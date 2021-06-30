import datetime
import os


# 获取当前时间
current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# time.format
select_time_one = datetime.datetime.strptime("2000-01-01 21:57:15","%Y-%m-%d %H:%M:%S")
select_time_two = datetime.datetime.strptime("2000-01-02 22:57:15","%Y-%m-%d %H:%M:%S")

# datetime to seconds regardless of days
seconds = (select_time_two - select_time_one).total_seconds()

# datetime to seconds considering days
total_seconds = (select_time_two - select_time_one).total_seconds()

# print time interval
start_time = datetime.datetime.now()
end_time = datetime.datetime.now() + datetime.timedelta(days=1)
print("time interval: " + str((end_time-start_time).total_seconds()) + "s")



