class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        stack=[]
        mini = min(strs, key=len)
        for i in range(0, len(mini)):
            prefix = strs[0][i]
            for j in range(1, len(strs)):
                if prefix != strs[j][i] and len(stack)==0:
                    return ""
                elif prefix != strs[j][i] and len(stack)!=0:
                    return "".join(stack)
            stack.append(prefix)
        return "".join(stack)