import sys
from datetime import date, datetime, time


def usage():
    print(f"Usage: {sys.argv[0]} <csv_file> -d \"yyyy-mm-dd\"")


if len(sys.argv) != 4 or sys.argv[2] != '-d':
    usage()
    exit(1)


allCookies = {}

cookie_log = open(sys.argv[1], "r")

date_time = datetime.strptime(sys.argv[3], "%Y-%m-%d")

for cur in cookie_log.readlines():
    cookie, timestamp = cur.split(",")
    timestamp = timestamp.replace("\n", "")
    tmp_datetime = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z')
    if date_time.strftime('%Y-%m-%d') == tmp_datetime.strftime('%Y-%m-%d'):
        if cookie in allCookies:
            allCookies[cookie] += 1
        else:
            allCookies[cookie] = 1


x = max(allCookies.values(), key= lambda x: x)

for cookie, y in allCookies.items():
    if y == x:
        print(cookie)

cookie_log.close()