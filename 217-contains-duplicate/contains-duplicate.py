class Solution(object):
    def containsDuplicate(self, nums):
        dset = set()
        for num in nums:
            if num in dset:
                return True
            else: dset.add(num)
        return False