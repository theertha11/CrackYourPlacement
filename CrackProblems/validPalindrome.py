class Solution:
    def validPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s)-1
        def isPalindrome(low, high, s):
            while low < high:
                if s[high] != s[low]:
                    return False  
                low += 1
                high -= 1 
            return  True  
        ans = isPalindrome(low, high, s)
        if ans:
            return True
        else:    
            while low < high:
                if s[high] == s[low]:
                    low += 1
                    high -= 1 
                else:
                    ans1 = isPalindrome(low+1, high, s)
                    if ans1:
                        return True
                    ans2 = isPalindrome(low, high-1, s)
                    if ans2:
                        return True
                    return False
            return True 