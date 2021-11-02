class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for ele in magazine:
            if ele in mag:
                mag[ele] += 1
            else:
                mag[ele] = 1
                
        for ele in ransomNote:
            if ele not in mag:
                return False
            if ele in mag:
                if mag[ele] < 1:
                    return False
            mag[ele] -= 1
        return True
        