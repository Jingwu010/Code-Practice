class Solution:
    class SortedList:
        def __init__(self):
            self.myList = []

        def insert(self, height, index):
            """
            insert (height, index) into the sortedlist
            sorted by height value
            return the value and index of the neareast smaller or equal element
            """
            if not self.myList:
                self.myList.append((height, index));
                return 0

            lens = len(self.myList)
            left, right = 0, lens - 1

            while left <= right:
                mid = (right + left) // 2
                midH, midI = self.myList[mid]
                if height == midH:
                    # self.myList[mid] = (height, index)
                    self.myList.insert(mid + 1, (height, index))
                    return mid + 1
                if height > midH:
                    left = mid + 1
                if height < midH:
                    right = mid - 1
            self.myList.insert(left, (height, index))
            return left
            
        def length(self):
            return len(self.myList)
        
        def remove(self, index):
            del self.myList[index]

        def getValue(self, index):
            return self.myList[index]

        def __str__(self):
            return ', '.join(map(str, self.myList))


    def trap(self, height, d=False):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        sl = self.SortedList()
        presum = [0]
        result = [0] * len(height)
        for i, h in enumerate(height):
            presum.append(presum[-1] + h)
            if d: print("standing at", i, "with heigh", h)
            idx = sl.insert(h, i)
            # if it is the highest point
            # find second highest (smaller or equal)
            if idx == sl.length() - 1:
                # if there is only 1 point
                if sl.length() == 1:
                    continue
                    
                # if second highest point exist
                # extract its value and index
                else:
                    lh, li = sl.getValue(idx - 1)
                    tmpTrap = lh * (i - li - 1) - (presum[i] - presum[li + 1])
                    result[i] = max(result[li] + tmpTrap, result[i-1])
                
            # if it is not the highest point
            # find the cloest higher point (higher or equal)
            else:
                for li in range(i-1, -1, -1):
                    if height[li] >= h:
                        tmpTrap = h * (i - li - 1) - (presum[i] - presum[li + 1])
                        result[i] = max(result[li] + tmpTrap, result[i-1])
                        break
            if sl.length() != 1 and sl.getValue(idx)[0] == sl.getValue(idx-1)[0]:
                sl.remove(idx-1)
        return result[-1]

