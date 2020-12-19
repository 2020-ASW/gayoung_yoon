def solution(k, room_number):
    answer = []
    check_room = {}
    for number in room_number:
        check_number = check_room.get(number, 0)

        if check_number:
            temp = [number]
            while True:
                idx = check_number
                check_number = check_room.get(check_number, 0)
                # print(check_number)
                
                if check_number == 0:  # check_number=0이면 없다는 것이므로 이곳에 넣어야함
                    # print('here')
                    answer.append(idx)
                    check_room[idx] = idx + 1
                    break

                temp.append(check_number)
                # print('answer')
                # print(answer)
                # print('check_number')
                # print(check_number)
                
        else:
            answer.append(number)
            check_room[number] = number + 1

    return answer

k = 10
room_number = [1,3,4,1,3,1]  # result = [1,3,4,2,5,6]

print(solution(k,room_number))