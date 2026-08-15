class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        lar,sec=0,0
        for i in nums:
            if i>=lar:
                sec=lar
                lar=i
            elif i>=sec:
                sec=i
        if sec*2<=lar:
            return nums.index(lar)
        return -1

