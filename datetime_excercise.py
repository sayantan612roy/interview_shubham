import datetime
start_time = '20:54:15.128800'
end_time = '20:54:26.513079'
def time_diff(start, end):
    start=  datetime.datetime.strptime(start, "%H:%M:%S.%f")
    end=  datetime.datetime.strptime(end, "%H:%M:%S.%f")
    return end - start

print(time_diff(start_time, end_time))
