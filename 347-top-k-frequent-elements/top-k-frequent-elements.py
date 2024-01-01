class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countDict = {}
        numFreq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            countDict[num] = 1 + countDict.get(num, 0)

        for n, c in countDict.items():
            numFreq[c].append(n)
        
        result = []

        for i in range(len(numFreq) - 1, 0, -1):
            for n in numFreq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        

            
        