k = 10
room_number = [1,3,4,1,3,1]

room = {}
check = []
for i in room_number:
    temp = i
    visit = [temp]
    while temp in room:
        temp = room[temp]
        visit.append(temp)
    check.append(temp)

    for v in visit:
        room[v] = temp + 1

print(check)