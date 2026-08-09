class numarray:
    def __init__(self,nums):
        self.prefix=[0]
        for num in nums:
            self.prefix.append(self.prefix[-1]+num)
    def sumrange(self,right,left):
        return self.prefix[right+1]-self.prefix[left]
