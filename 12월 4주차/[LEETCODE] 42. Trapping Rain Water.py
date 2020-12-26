# Two Pointer

height = [0,1,0,2,1,0,1,3,2,1,2,1]  # 6
# height = [4,2,0,3,2,5]  # 9

def trap(self, height):
    if not height:
        return 0

    answer = 0
    left_index, right_index = 0, len(height) - 1
    left, right = height[left_index], height[right_index]
    while left_index < right_index:
        left, right = max(left, height[left_index]), max(right, height[right_index])

        if left <= right:
            answer += left - height[left_index]
            left_index += 1
        else:
            answer += right - height[right_index]
            right_index -= 1

    return answer

'''
height = [0,1,0,2,1,0,1,3,2,1,2,1]
===================================
left_index, right_index
2 11
left, right
1 1
answer
1
------------------------------------
left_index, right_index
3 11
left, right
2 1
answer
1
------------------------------------
left_index, right_index
3 10
left, right
2 2
answer
1
------------------------------------
left_index, right_index
4 10
left, right
2 2
answer
2
------------------------------------
left_index, right_index
5 10
left, right
2 2
answer
4
------------------------------------
left_index, right_index
6 10
left, right
2 2
answer
5
------------------------------------
left_index, right_index
7 10
left, right
3 2
answer
5
------------------------------------
left_index, right_index
7 9
left, right
3 2
answer
6
------------------------------------
left_index, right_index
7 8
left, right
3 2
answer
6
------------------------------------
'''