class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        result = []
        for i in range(len(freq)-1, -1, -1):
            for number in freq[i]:
                if len(result) == k:
                    return result

                result.append(number)

        return result
