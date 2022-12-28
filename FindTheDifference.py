class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sdic = Counter(s)
        for char in t:
            if char in sdic and sdic[char]:
                sdic[char] -= 1
            else:
                return char
