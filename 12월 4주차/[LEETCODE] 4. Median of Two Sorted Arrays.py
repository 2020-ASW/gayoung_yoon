def findMedianSortedArrays(self, nums1, nums2):
    nums = nums1 + nums2
    nums = sorted(nums)

    x = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[x] + nums[x-1]) / 2
    else:
        return nums[x]
