class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {"(":")", "[":"]", "{":"}"}
        for ele in s:
            if ele == '(' or ele == '[' or ele == '{':
                stack.append(ele)
            else:
                if len(stack)!=0:
                    if dct[stack[len(stack)-1]] == ele:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                    
                    
                    
            
        