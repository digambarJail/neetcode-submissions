class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mydict = {}

        for num in nums:
            if num not in mydict:
                mydict[num] = 1
            else:
                mydict[num] += 1

        sorted_dict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))

        answer = []
        for key, val in sorted_dict.items():
            answer.append(key)
            if len(answer) == k:
                break

        return answer