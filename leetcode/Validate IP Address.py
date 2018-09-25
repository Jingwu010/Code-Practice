class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        def validateIPv4(IP):
            digits = IP.split('.')
            if len(digits) != 4:
                return False
            for digitstr in digits:
                if len(digitstr) > 3 or len(digitstr) <= 0:
                    return False
                try: 
                    digit = int(digitstr)
                except: 
                    return False
                # check range
                if digit > 255 or digit < 0:
                    return False
                # check leading 0s
                if len(str(digit)) != len(digitstr):
                    return False
            return True
        
        def validateIPv6(IP):
            hexDigits = IP.split(':')
            if len(hexDigits) != 8:
                return False
            for hexDigitStr in hexDigits:
                if len(hexDigitStr) > 4 or len(hexDigitStr) <= 0:
                    return False

                for char in hexDigitStr:
                    # check hexadecimal digit
                    try:
                        int(char)
                    except:
                        if ord(char.lower()) - ord('a') < 0 or \
                            ord(char.lower()) - ord('a') > 5:
                            return False
            return True

        if validateIPv4(IP):
            return 'IPv4'
        elif validateIPv6(IP):
            return 'IPv6'
        else:
            return 'Neither'

# print(Solution().validIPAddress("172.16.254.1"))
# print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
# print(Solution().validIPAddress("256.256.256.256"))
# print(Solution().validIPAddress("172.16.254.01"))
# print(Solution().validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334"))
# print(Solution().validIPAddress("2001:0db8:85a3::8A2E:0370:7334"))
# print(Solution().validIPAddress("10:0df8:85a3:0:0:8a2e:037:7334"))
# print(Solution().validIPAddress("120.25.2.10"))
