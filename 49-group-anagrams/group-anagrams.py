class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        countMap = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord("a")] += 1
            countMap[tuple(count)].append(str)
        return countMap.values()