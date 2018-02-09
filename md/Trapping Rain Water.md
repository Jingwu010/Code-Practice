## 42. [Trapping Rain Water](https://github.com/GrEedWish/Code-Practice/blob/master/leetcode/Trapping%20Rain%20Water.py)

Given *n* non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. 

For example, 
Given `[0,1,0,2,1,0,1,3,2,1,2,1]`, return `6`.

![img](https://leetcode.com/static/images/problemset/rainwatertrap.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. **Thanks Marcos** for contributing this image!



#### My Solution:

Starting from the left, if we encounter a bar with evaluation `h`, there exist 2 possible cases that could trap rain:

1. the bar `h`is the highest bar as far from left and we need to find a second highest from its left to trap as much water as possible. (The second highest could be lower or equal to `h`)
2. the bar `h` is not the highest bar as far from left and we need to find the closest bar which has evaluation higher or equal to `h`

To sum up, the equation should look like:

`trapAmount = height * (right index - left index)- base` 

[base is the areas occupied by bars, we can calculate this by prefix sum]

Take  `[0,1,0,2,1,0,1,3,2,1,2,1]` as example:

First stand at 0, its the only bar as far, continue;

stand at 1, its the highest bar as far, the second highest bar is 0 and its index is 0, the trap amount is $0 \times (1-0) - base$  

stand at 0, its not the highest bar as far, the closest highest bar is 1 and its index is 1, the trap amount is $0 \times (2-2) - base$ 

stand at 2, its the highest bar as far, the second highest bar is 1 and its index is 1, the trap amount is $1 \times (3-2) - base$ 

More general, if we stand at index `ri` (right index) with its value `rh` (right height), we find another bar satisfy the above two condition at index `li` (left index) with its value `lh` (left height), we can calculate the trap amount between the two bar is

`trapAmount = min(lh, rh) * (ri - li - 1)- base`

Here raise the question, how to get `li` and `lh`?

1. If `rh` is the highest bar as far, we want to know the second or same highest bar index, we can use a sorted list to record each height and its index, if we stand at 2 at index 3, then the sorted list looks like:

   `[(0,2), (1,1), (2,3)]`

   Then we know the second highest is value 1 at index 1, which is left to the `(2,3)`. If there is some same height in the list, we can keep it like:

   `[(0,2), (1,1), (2,0), (2,3)]`

   and then we know the same highest on the left is value 2 at index 0, which is left to `(2,3)`. After this step, simply delete `(2,0)`and continue.

2. If `rh` is not the highest bar as far, we want to know what is the closest bar has evaluation greater or equal than `rh` at index  `ri`. then we can scan the height list from `ri` to `0`, whenever we encounter a evaluation `>=` than `rh`, we can say the bar is the`lh` and `li`. 

Then, we still need to calculate the total amount of water trapped by using dynamic programming idea, that is, for a given bar at index `ri`, its total amount of water trapped is:

`total[ri] = max(total[ri-1], trapAmount + total[ri - li])`

In the end, the time complexity of this algorithm is O(n) in average and space complexity is O(n)

```Python
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
```





#### Better Solution:

maintain a max height of the left and max height of the right, traveling from two ends to the middle, which should be the highest bar. Whenever we come into a bar has smaller evaluation than left max (from left hand side) or right max (from right hand side), the fill it with water, if we come into a bar has same or bigger evaluation than left max or right max, we reset the max.

Take  `[0,1,0,2,1,0,1,3,2,1,2,1]` as example:

left is index 0 (evaluation 0), right is index 11 (evaluation 1)

0 is smaller than 1, we make left = left + 1 and maxleft = 1

1 is smaller (equal) than 1, we make left = left + 1 and fill with water maxleft - height[left] = 1 -  0 = 1

0 is smaller than 1, we make left = left + 1 and maxleft = 2

2 is bigger than 1, which could be the highest bar, so we make right = right - 1, and rightmax = 2

2 is smaller (equal) than 2, we make left = left + 1, and fill with water maxleft - height[left] = 2 - 1 = 1

1 is smaller than 2, we make left = left + 1, and fill with water maxleft - height[left] = 2 - 0 = 2

0 is smaller than 2, we make left = left + 1, and fill with water maxleft - height[left] = 2 - 1 = 1

1 is smaller than 2, we make left = left + 1, and maxleft = 3

3 is bigger than 2, we make right = right - 1, and fill with water maxright - height[right] = 2 - 1 = 1

3 is bigger than 1, we make right = right - 1, and set rightmax = 2

3 is bigger than 2, we make right = right - 1, and set rightmax = 3

left = right and we are done

So simple and so neat!

```Python
def trap(height):
    left, right = 0, len(height) - 1
    leftmax, rightmax = 0, 0
    res = 0
    while left < right:
        if height[left] <= height[right]:
            if height[left] >= leftmax: leftmax = height[left]
            else: res += leftmax - height[left]
            left += 1
        else:
            if height[right] >= rightmax: rightmax = heigh[right]
            else: res += rightmax - height[right]
            right -= 1
     return res
```

In the end, the time complexity of this algorithm is O(n) and space complexity is O(1)



#### Some Insights

The trick here is instead of **scanning from left to right**, we can dramatically improve the performance by **scanning from left and right to middle**.
