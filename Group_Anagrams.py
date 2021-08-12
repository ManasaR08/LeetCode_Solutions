class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in dct:
                dct[sorted_word].append(word)
            else:
                dct[sorted_word] = [word]
        values = dct.values()
        return list(values)
