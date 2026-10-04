class Solution:
    def intToRoman(self, num: int) -> str:
        val=[["M",1000],["CM",900],["D",500],["CD",400],["C",100],["XC",90],["L",50],["XL",40],["X",10],["IX",9],["V",5],["IV",4],["I",1]]
        res=''
        for sym,dig in val:
            if num//dig:
                count=num//dig
                res=res+(sym*count)
                num=num%dig
        return res



        