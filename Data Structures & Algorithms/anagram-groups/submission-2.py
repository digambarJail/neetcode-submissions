class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())

        

        res = defaultdict(list)
        for s in strs:
            myarr = [0] * 26
            for char in s:
                position = ord(char.lower()) - ord('a') 
                myarr[position] += 1
            res[tuple(myarr)].append(s)

        return list(res.values())