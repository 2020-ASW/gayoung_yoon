class Solution:
    def maxArea(self, height):
        start, end = 0, len(height) - 1
        y_height = 0

        mymax = 0
        while end > start:
            container = (end - start) * min(height[end], height[start])
            if mymax < container:
                mymax = container
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return mymax



height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
# height = [4,3,2,1,4]
# height = [1,2,1]

print(Solution.maxArea(height))