walk_h = int(input())
walk_min = int(input())
walk_sec = int(input())
rain_h = int(input())
rain_min = int(input())
rain_sec = int(input())
hours = rain_h - walk_h
minutes = rain_min - walk_min
sec = rain_sec - walk_sec
sec_overall = sec + 60 * minutes + 60 ** 2 * hours
print(sec_overall)
