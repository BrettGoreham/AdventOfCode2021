import json
import pytz
from datetime import datetime
from datetime import timezone
from datetime import timedelta


def sort_first_star(e):
    day_res = e["completion_day_level"].get(day, None)
    if day_res is None:
        return float('inf')
    return day_res['1']["get_star_ts"]


def sort_second_star(e):
    day_res = e["completion_day_level"].get(day, None)
    if day_res is None:
        return float('inf')
    part2 = day_res.get('2', None)
    if part2 is None:
        return float('inf')
    return part2["get_star_ts"]


def sort_time_between_stars(e):
    day_res = e["completion_day_level"].get(day, None)
    if day_res is None:
        return float('inf')

    _starOne = day_res['1']["get_star_ts"]
    day2 = day_res.get('2', None)
    if day2 is None:
        return float('inf')
    _starTwo = day2["get_star_ts"]
    return _starTwo - _starOne


def find_longest_name(members_list):
    longest = 0
    for mem in members_list:
        if len(mem['name']) > longest:
            longest = len(mem['name'])
    return longest


# Opening JSON file
with open('leaderboard.json', encoding='utf-8') as f:
    # returns JSON object as
    # a dictionary
    data = json.load(f)

day = "12"
osloTz = pytz.timezone("Europe/Oslo")
topXResults = 6

membersList = (list(data["members"].values()))

print('Top ' + str(topXResults) + ' quickest star 1 for day ' + str(day))
print()

membersList.sort(key=sort_first_star)
nameLen = find_longest_name(membersList[:topXResults])
for member in membersList[:topXResults]:
    ts = member["completion_day_level"][day]['1']["get_star_ts"]
    print(member["name"].ljust(nameLen) + ' ' + datetime.fromtimestamp(ts, tz=osloTz).strftime('%H:%M:%S %d-%m-%Y'))


print()
print('Top ' + str(topXResults) + ' quickest star 2 for day ' + str(day))
print()
membersList.sort(key=sort_second_star)
nameLen = find_longest_name(membersList[:topXResults])
for member in membersList[:topXResults]:
    ts = member["completion_day_level"][day]['2']["get_star_ts"]
    print(member["name"].ljust(nameLen) + ' ' + datetime.fromtimestamp(ts, tz=osloTz).strftime('%H:%M:%S %d-%m-%Y'))


print()
print('Quickest time between star 1 and star 2 for day ' + str(day))
print('')
membersList.sort(key=sort_time_between_stars)
nameLen = find_longest_name(membersList[:topXResults])
for member in membersList[:topXResults]:
    ts1 = member["completion_day_level"][day]['1']["get_star_ts"]
    ts2 = member["completion_day_level"][day]['2']["get_star_ts"]
    time1 = datetime.fromtimestamp(ts1, tz=osloTz)
    time2 = datetime.fromtimestamp(ts2, tz=osloTz)
    timeBetween = time2 - time1

    print(member["name"].ljust(nameLen) + ' ' + str(timeBetween))

