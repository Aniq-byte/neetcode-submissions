class Solution:
    def isValid(self, s: str) -> bool:

        stack = list('' for i in  range(len(s)))
        size = 0

        for c in s:

            if c == ')':

                if size == 0:
                    return False

                if stack[size - 1] == '(':
                    size -= 1
                else:
                    return False

            elif c == '}':

                if size == 0:
                    return False
                    
                if stack[size - 1] == '{':
                    size -= 1
                else:
                    return False

            elif c == ']':

                if size == 0:
                    return False
                    
                if stack[size - 1] == '[':
                    size -= 1
                else:
                    return False
            
            else:
                stack[size] = c
                size += 1
        
        if size == 0:
            return True
        
        return False


        