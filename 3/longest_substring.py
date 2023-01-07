from ast import List


class Solution:
    # not working
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)   
        if l == 0: return 0
        if l == 1: return 1       

        current = []
        tmpMax = 0
        currentMax = 1

        for ch in s:
            if not (ch in current):
                tmpMax += 1
                current.append(ch)
            else:
                if tmpMax > currentMax:
                    currentMax = tmpMax
                tmpMax = 1
                print(current)
 
        currentMax = max(currentMax, tmpMax)
        return currentMax
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":

    print(Solution().lengthOfLongestSubstring2("pwwkew")) # 3
    print(Solution().lengthOfLongestSubstring2("a")) # 1
    print(Solution().lengthOfLongestSubstring2("au")) # 2
    print(Solution().lengthOfLongestSubstring2("dvdf")) # 3
