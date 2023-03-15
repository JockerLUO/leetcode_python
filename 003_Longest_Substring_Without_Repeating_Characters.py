class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = [range(len(s))]
        cMap = {}
        maxL = 0
        start = 0
        for i in range(len(s)):
            c = s[i]
            if c in cMap.keys():
                start = max(start, cMap[c])
            cMap[c] = i + 1
            maxL = max(maxL, i - start + 1)
        return maxL

if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("abcabcbb")
    print(res)