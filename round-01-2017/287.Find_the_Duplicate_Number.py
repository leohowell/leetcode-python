# -*- coding: utf-8 -*-


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow

s = Solution()
print s.findDuplicate([1,1])
