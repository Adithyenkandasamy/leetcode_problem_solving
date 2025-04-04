def reverseBits(n: int) -> int:
        result = 0
        for _ in range(32):
            bit = n & 1                   
            result = (result << 1) | bit  
            n >>= 1                       
        return result
x = "00000010100101000001111010011100"
n = int(x, 2)
result = reverseBits(n)
print(result)
