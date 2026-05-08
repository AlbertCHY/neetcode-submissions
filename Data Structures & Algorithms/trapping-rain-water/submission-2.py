class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        # leftbound, rightbound = 0, len(height) - 1
        # while leftbound + 1 < len(height) and height[leftbound] <= height[leftbound + 1]:
        #     leftbound += 1
        # while rightbound - 1 >= 0 and height[rightbound] <= height[rightbound - 1]:
        #     rightbound -= 1
        # if leftbound >= rightbound or leftbound == len(height) - 1 or rightbound == 0:
        #     return 0

        water = 0
        # left, right = leftbound, rightbound
        left, right = 0, len(height) - 1
        while left < right:
            
            if height[left] <= height[right]:
                prev_idx = left
                prev_h = height[left]
                while left < right and height[left] <= prev_h:
                    water += prev_h - height[left]
                    left += 1
            else:
                prev_idx = right
                prev_h = height[right]
                while left < right and height[right] <= prev_h:
                    water += prev_h - height[right]
                    right -= 1


        return water