class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest=max(candies)
        lis=[]
        for i in candies:
            if i+extraCandies>=greatest:
                lis.append(True)
            else:
                lis.append(False)
        return lis