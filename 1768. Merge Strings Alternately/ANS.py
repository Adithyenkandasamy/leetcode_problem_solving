class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=[]
        min_length = min(len(word1),len(word2))
        max_length = max(len(word1),len(word2))
        for i in range(min_length):
            result.append(word1[i])
            result.append(word2[i])    
        if len(word1) > len(word2):
            for i in range(min_length,max_length):
              result.append(word1[i])
        else:
            for i in range(min_length,max_length):
              result.append(word2[i])
        return ''.join(result)

# efficient solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            ans = ''.join(a+b for a,b in zip(word1,word2)) + word1[len(word2):]
        elif len(word1) < len(word2):
            ans = ''.join(a+b for a,b in zip(word1,word2)) + word2[len(word1):]
        else:
            ans = ''.join(a+b for a,b in zip(word1,word2))
        return ans
