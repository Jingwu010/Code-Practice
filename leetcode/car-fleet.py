class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        def sortPosition(position, speed):
            # sort position into descending order and speed accordingly
            # return a tupleList where first element is position and second element is speed
            
            tupleList = [(x, y) for x, y in zip(position, speed)]
            tupleList.sort(key=lambda x: x[0], reverse=True)
            return tupleList

        tupleList = sortPosition(position, speed)
        timeNeeded = [(target-x[0])/x[1] for x in tupleList]
        print(timeNeeded)
        for i in range(1, len(timeNeeded)):
            if timeNeeded[i] < timeNeeded[i-1]:
                timeNeeded[i] = timeNeeded[i-1]
        return len(set(timeNeeded))

print(Solution().carFleet(12,[10,8,0,5,3], [2,4,1,1,3]))