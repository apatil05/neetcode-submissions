class Solution:
    def isValid(self, s: str) -> bool:
        """
        Stack --> every time we encounter char in ['{','(','['] we push it on the stack
        
        ever time we encounter char in the complement we pop from the stack

        return true if our stack isEmpty()

        false otherwise
        """
        validStack = []
        for char in s:
            if char in ['{','(','[']:
                validStack.append(char)
            else:
                if not validStack:
                    return False

                top = validStack[-1]
                if top == '{':
                    complement = '}'
                elif top == '[':
                    complement = ']'
                elif top == '(':
                    complement = ')'
                else:
                    print("unidentified char")
                
                if char == complement:
                    validStack.pop()
                else:
                    return False
        
        if not validStack:
            return True
        else:
            return False

            
