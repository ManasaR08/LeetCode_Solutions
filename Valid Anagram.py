class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        for ele in s:
            if ele in ss:
                ss[ele] += 1
            else:
                ss[ele] = 1
        
        for ele in t:
            if ele not in ss:
                return False
            if ele in ss:
                ss[ele] -= 1
                if ss[ele] == 0:
                    del ss[ele]
                    
        if len(ss) != 0:
            return False
        return True
        