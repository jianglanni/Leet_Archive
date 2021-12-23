class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        farthest = {}
        for i in range(len(s)):
            farthest[s[i]] = i
        ret = []
        pin = -1
        while pin < len(s):
            pos = pin+1
            if pos == len(s):
                break
            pin = farthest[s[pos]]
            pos += 1
            while pos <= pin:
                pin = max(pin, farthest[s[pos]])
                pos += 1
            ret.append(pin)
        for i in range(1, len(ret))[::-1]:
            ret[i] -= ret[i-1]
        ret[0] += 1
        return ret


def main():
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))  # Test case


if __name__ == "__main__":
    main()
