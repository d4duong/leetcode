from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        # Kadane's Algorithm
        # Keep track of two things: 
            # 1) Largest sum of array that must end at current index
                # Here you have two choices:
                    # 1) Start new sub array at this index
                    # 2) Extend current sub array which ends at this index
            # 2) Best sum overall
        
        end = best = nums[0]
        for n in nums[1:]:
            end = max(n, end + n)
            best = max(best, end)
        return best

def test():
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert s.maxSubArray(nums) == 6