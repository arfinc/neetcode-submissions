class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {} #hashmap storing key (integer) and value (how often)

        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
    
        i = sorted((frequency.items()), key = lambda x: x[1],reverse = True)
        return [x[0] for x in i[0:k]]