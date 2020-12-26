# 재귀사용했는데 for word있는 부분에서 어떻게 처리해야할지 시간걸림.

# class Solution:
def partition(s):

    def go(s, part):
        if not s:
            answer.append(part)
        
        for i in range(len(s)):
            if checkPalindrome(s[:i+1]):
                go(s[i+1:], part+[s[:i+1]])

    def checkPalindrome(s):
        return s == s[::-1]
    
    answer = []
    go(s, [])
    return answer
    
print(partition("aabaa"))