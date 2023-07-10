class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(','{','[']
        right = [')','}',']']
        stack = []
        flag =0

        if len(s) % 2 != 0 :
            return False
        elif s[0] in right:
            return False
        else:
            for j in range(0, len(s)):
                c = s[j]
                if c in left:
                    stack.append(c)
                    continue
                elif len(stack) == 0 and c in right:
                    flag=1
                    break
                else:
                    last = stack[-1]
                    i = left.index(last)
                    match = right[i]

                    if match == c:
                        stack.pop()
                    else:
                        flag=1
                        break
            if len(stack) == 0 and flag == 0:
                return True
            elif len(stack) != 0 and flag == 1:
                return False