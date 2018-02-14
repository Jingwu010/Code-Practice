class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        i = 0 
        j = len(nums) - 1
        while i < j:
            sums = sorted_nums[i] + sorted_nums[j]
            if sums == target:
                break
            elif sums > target:
                j = j - 1
            elif sums < target:
                i = i + 1
        ans_nums = [sorted_nums[i], sorted_nums[j]]
        ans = []
        index = 0
        while ans_nums:
            if nums[index] in ans_nums:
                ans.append(index)
                ans_nums.remove(nums[index])
            index = index + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 3, 2, 2], 5))
    print(s.twoSum([2, 7, 11, 15], 9))
