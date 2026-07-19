class Solution:
    def isValidIP4(self, ip4: str) -> bool:
        nSegments = 0
        length = 0
        num = 0

        for ch in ip4:
            if ch == '.':
                if length == 0 or length > 3 or num > 255:
                    return False
                num = 0
                length = 0
                nSegments += 1
            elif ch.isdigit():
                # Leading 0 not allowed
                if length == 1 and num == 0:
                    return False
                num = num * 10 + int(ch)
                length += 1
            else:
                return False
        
        # Validate last segment
        if length == 0 or num > 255:
            return False
        nSegments += 1
        return nSegments == 4


    def isValidIP6(self, ip6: str) -> bool:
        nSegments = 0
        length = 0

        for ch in ip6:
            if ch == ':':
                if length == 0 or length > 4:
                    return False
                length = 0
                nSegments += 1
            elif ch in "0123456789abcdefABCDEF":
                length += 1
            else:
                return False
        
        # Validate last segment
        if length == 0 or length > 4:
            return False
        nSegments += 1
        return nSegments == 8



    def validIPAddress(self, queryIP: str) -> str:
        if self.isValidIP4(queryIP):
            return "IPv4"
        elif self.isValidIP6(queryIP):
            return "IPv6"
        else:
            return "Neither"
