class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # Q1: Can any of the jug has an volume of zero?
        # Q2: Can z be composed from x and y?
        a = min(x, y)
        b = max(x, y)
        collection = set([a, b])
        combination = set([a+b])
        multiplier = 2
        while 0 not in collection:
            # use the larger jug as container
            # the smaller one as increment step
            # so the possibile combination is n*a%b
            # whenever there is a repeation in the reminder
            # then we end
            remainder = (a * multiplier) % b
            if remainder in collection:
                break
            collection.add(remainder)
            if remainder <= a:
                combination.add(remainder + b)
            if remainder <= b:
                combination.add(remainder + a)
            multiplier += 1
        print(collection)
        print(combination)
        if z in collection or z in combination:
            return True
        return False

# If GCD(x, y) == 1?

print(Solution().canMeasureWater(3,5,4))
print(Solution().canMeasureWater(2,6,5))
print(Solution().canMeasureWater(2,5,6))
print(Solution().canMeasureWater(13,7,24))
print(Solution().canMeasureWater(1,2,3))
