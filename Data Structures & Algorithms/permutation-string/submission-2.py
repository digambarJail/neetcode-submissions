class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        expected_dict = {}
        for char in s1:
            expected_dict[char] = 1 + expected_dict.get(char, 0)

        r = 0
        for l in range(len(s2)):
            curr_dict = {}
            if s2[l] not in expected_dict.keys():
                continue
            
            r = l
            while r < len(s2):
                curr_dict[s2[r]] = 1 + curr_dict.get(s2[r], 0)
                if s2[r] in curr_dict.keys() and s2[r] not in expected_dict.keys():
                    curr_dict = {}
                    break
                if curr_dict[s2[r]] > expected_dict[s2[r]]:
                    curr_dict = {}
                    break
                if curr_dict == expected_dict:
                    return True
                r += 1


        return False