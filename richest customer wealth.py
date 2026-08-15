class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for  i in accounts:
            summ=0
            for j  in i:
                summ+=j
            maxi=max(summ,maxi)
        return maxi

        