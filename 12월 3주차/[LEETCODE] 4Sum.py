'''
정렬 후, a,b,c,d를 결정해야한다.
4중for문보다 a, b는 for문으로 결정하고, c,d는 while문 이용
'''

# class Solution:
def fourSum(nums, target):
    nums = [1,0,-1,0,-2,2]
    target = 0
    nums = sorted(nums)
    nums_len = len(nums)

    # a, b를 설정하고 나서 c, d도 설정해야하기때문에
    # for문 돌린 후 2개 값을 설정할 수 있어야한다. 
    check = set()
    for a in range(len(nums) - 3):
        for b in range(a + 1, len(nums) - 2):
            new_target = target - nums[a] - nums[b]

            c, d = b + 1, nums_len - 1
            while d > c:
                if new_target == nums[c] + nums[d]:
                    check.add((nums[a], nums[b], nums[c], nums[d]))
                    c += 1
                    d -= 1

                elif new_target > nums[c] + nums[d]:
                    c += 1

                else:
                    d -= 1

    return list(check)

# nums = [1,0,-1,0,-2,2]
# target = 0
# print(fourSum(nums, target))