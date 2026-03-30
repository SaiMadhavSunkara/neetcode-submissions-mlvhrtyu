class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        new_num = []
        highest_num = 0 
        for i in range(len(nums)):
            if nums[i] in record:
                record[nums[i]] += 1
            else:
                record[nums[i]] = 1
        for _ in range(k):
            highest_num = 0
            highest_freq = 0
            for i in record:
                if highest_freq <= record[i] and i not in new_num:
                    highest_freq = record[i]
                    highest_num = i
            new_num.append(highest_num)
        return new_num
            
