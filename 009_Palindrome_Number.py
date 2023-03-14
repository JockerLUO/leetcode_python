class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        s = str(x)
        i = 0
        mid = int((len(s) + 1) / 2)
        while i <= mid:
            if s[i] != s[len(s) - 1 - i]:
                return False
            i += 1
        return True

if __name__ == '__main__':
    s = Solution()
    res = s.isPalindrome(1)
    print(res)
    