'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
'''


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i + 1:]:
                return [i, nums[i + 1:].index(res) + i + 1]


test = Solution()
print(test.twoSum([2, 7, 11, 15], 9))
