def macs(numList):
    stack = []
    maxArea = 0
    for i in range(len(numList)):
        area = 0
        # if the stack is not empty
        # which means there is a constrain beforehand
        while stack:
            # take the constrain info out 
            top, idx, idx_area = stack[-1]
            # if the current number is greater than the constrain
            # add the current number as a new constrain in the stack
            # for the later numbers coming into the stack
            if numList[i] > top:
                # Maximum area is considering the minimum height from new constrain
                # or the minimum height from the previous constrain 
                area = max(numList[i]*(i-idx), idx_area+top)
                break
            # else if current number is smaller or equal to constrain
            # compress the constrain by poping out 
            # the previous constrain in the stack 
            else:
                stack.pop()

        # if stack is empty
        if not stack:
            area = numList[i] * (i + 1)

        # add the constrain into the stack
        # DEF: A constrain is, the height, the index,
        # and the maximum area that ending at it from the left
        stack.append((numList[i], i, area))
        # compare the maxArea
        maxArea = max(area, maxArea)
    return maxArea
            
print(macs([4,2,3,2,1,3,4,3]))
print(macs([1,1,5,5,5,1]))
print(macs([3,1,3,2]))

print(macs([1,5,2,3]))
print(macs([3,2,5,1]))

print(macs([]))