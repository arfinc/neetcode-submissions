class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = []
        maximum = []

        for num in nums:
            if num == 1:
                count.append(num)
                maximum.append(len(count))
            if num != 1:
                maximum.append(len(count))
                count.clear()

        return max(maximum)


