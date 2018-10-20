
class Date(object):
    
    MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def __init__(self, string):
        segs = string.split()
        print(segs[0])
        self.date = int(segs[0])
        self.month = self.MONTHS.index(segs[1])
        self.year = int(segs[2]) 

    def __lt__(self, other):
        # Compare the year
        print(self.date, self.month, self.year)
        if self.year > other.year:
            return False
        elif self.year < other.year:
            return True
        else:
            # Compare the month
            if self.month > other.month:
                return False
            elif self.month < other.month:
                return True
            else:
                # Compare the date
                if self.date > other.date:
                    return False
                else:
                    return True

def sortDates(dates):
    """
    :type dates: List[string]
    :rtype: List[string]
    """

    return sorted(dates, key=Date)

# print(sortDates(['01 Mar 2017', '01 Mar 2017', '15 Jan 1998', '15 May 1998', '5 Jan 1998']))
# print(Solution().sortDates(['01 Mar 2017', '03 Feb 2017', '28 Feb 2018','15 Jan 1998']))
print(sortDates(['20 Oct 2052','06 Jun 1933','26 May 1960','20 Sep 1958','16 Mar 2068','25 May 1912','16 Dec 2018','26 Dec 2061','04 Nov 2030','28 Jul 1963']))



