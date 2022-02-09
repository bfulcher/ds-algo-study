class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        count = 0
        
        if k == 0:
            for key, value in counter.items():
                if value>1:
                    count+=1
        else:   
            for key, value in counter.items():
                if key+k in counter:
                    count+=1
                
        return count
