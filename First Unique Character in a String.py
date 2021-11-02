class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
                
        for ele in list(count.keys()):
            if count[ele] == 1:
                return s.find(ele)
        return -1
        