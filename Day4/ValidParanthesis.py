# def isValid(s: str) -> bool:
#     stack=[]
#     mapping ={')':'(' ,']':'[', '}':'{'}

#     for ch in s:
#         if ch in mapping:
#             if not stack or stack.pop != mapping[ch]:
#                 return False
#         else:
#             stack.append(ch)
#     return len(stack)==0

def isValid(s) -> bool:
    stack = []
    for ch in s:
        if ch == '(' or ch =='[' or ch=='{':
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            
            top = stack.pop() 

            if ch==')' and top != '(':
                return False
            if ch==']' and top!='[':
                return False
            if ch=='}' and top!='{':
                return False
    return len(stack)==0


s="()[]{}"
print(isValid(s))