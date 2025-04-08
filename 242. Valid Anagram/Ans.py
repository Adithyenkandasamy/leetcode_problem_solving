# 242. Valid Anagram


def isAnagram(s,t):
    x,y = sorted(s),sorted(t)
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        if x[i] != y[i]:
            return False
    return True
# Test cases
print(isAnagram("anagram","nagaram")) # True