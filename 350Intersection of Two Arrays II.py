class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct1 = {}
        dct2 = {}
        for ele in nums1:
            if ele in dct1.keys():
                dct1[ele] += 1
            else:
                dct1[ele] = 1
        for ele in nums2:
            if ele in dct2.keys():
                dct2[ele] += 1
            else:
                dct2[ele] = 1
        result = []
        common = dct1.keys() & dct2.keys()
        for com in common:
            while(dct1[com] != 0 and dct2[com] != 0):
                result.append(com)
                dct1[com] -= 1
                dct2[com] -= 1
        return result 