class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100, 'D': 500, 'M': 1000
}
        res=mp[s[-1]]
        for i in range(1,len(s)):
            if mp[s[i-1]]<mp[s[i]]:
                res-=mp[s[i-1]]
            else:
                res+=mp[s[i-1]]
        return res