class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        # special case, any one of the array is empty, the result is empty array
        if len(nums1) <= 0 or len(nums2) <= 0:
            return []
        
        i = 0 # index for nums1
        j = 0 # index for nums2
        flag = [[0 for j in range(len(nums2))] for i in range(len(nums1))]
        maxHeap = []
        results = []
        maxHeap.append((nums1[i]+nums2[j], i, j))

        while len(maxHeap) > 0 and k > 0:
            minPair = maxHeap.pop()
            k -= 1

            i = minPair[1]
            j = minPair[2]
            results.append([nums1[i], nums2[j]])

            if i+1 < len(nums1) and flag[i+1][j] == 0:
                newPair1 = (nums1[i+1]+nums2[j], i+1, j)
                maxHeap.append(newPair1)
                flag[i+1][j] = 1
            if j+1 < len(nums2) and flag[i][j+1] == 0:
                newPair2 = (nums1[i]+nums2[j+1], i, j+1)
                maxHeap.append(newPair2)
                flag[i][j+1] = 1

            maxHeap = sorted(maxHeap, key = lambda x : -x[0])

            # print('maxHeap', maxHeap)

        return results

# print('?')
# print(Solution().kSmallestPairs([1,7,11], [2,4,6], 100))
# print(Solution().kSmallestPairs([1,1,2], [1,2,3], 15))
# print(Solution().kSmallestPairs([1,2], [3], 3))



