class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        mydict1 = {}
        mydict2 = {}

        for i in range(len(s)):
            if s[i] not in mydict1:
                mydict1[s[i]] = 1
            else:
                mydict1[s[i]] += 1

            if t[i] not in mydict2:
                mydict2[t[i]] = 1
            else:
                mydict2[t[i]] += 1

        return mydict1 == mydict2