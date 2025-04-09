from typing import List

def reverseString( s: List[str]) -> None:
        s[:] = s[::-1]
        return s 
s = ["h","e","l","l","o"]
print(reverseString(s))