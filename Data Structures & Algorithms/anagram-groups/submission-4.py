class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mydict = defaultdict(list)
        for mystr in strs:
            myarr = [0] * 26
            for char in mystr:
                myarr[ord(char)-ord('a')] += 1
            
            mydict[tuple(myarr)].append(mystr)

        return list(mydict.values())