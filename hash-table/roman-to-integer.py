class Solution:
    def romanToInt(self, s: str) -> int:
        """
        intVal = 0
        mapRomanInt = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        j = 9999
        for i in range(len(s)-1):
            if i==j:
                continue
            if (s[i]=="I" and (s[i+1]=="V" or s[i+1]=="X")) or (s[i]=="X" and (s[i+1]=="L" or s[i+1]=="C")) or (s[i]=="C" and (s[i+1]=="D" or s[i+1]=="M")):
                intVal=intVal+mapRomanInt[s[i+1]]-mapRomanInt[s[i]]
                j = i+1
                continue
            intVal=intVal+mapRomanInt[s[i]]
        if j!=len(s)-1:
            intVal=intVal+mapRomanInt[s[-1]]
        return intVal
        """
        mapRomanInt = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        for i in range(len(s)-1):
            curr, nex = mapRomanInt[s[i]], mapRomanInt[s[i+1]]
            if curr<nex:
                ans = ans - curr
            else:
                ans = ans + curr
        return ans+mapRomanInt[s[-1]]


                