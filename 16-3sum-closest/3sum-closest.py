class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        n = len(nums)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target
                    
        return closest_sum