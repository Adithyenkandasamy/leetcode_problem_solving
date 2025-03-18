class Solution:
    def intToRoman(self, num: int) -> str:
        num_maps={
            1:"I",
            4:"IV",
            5:"V",
            9:"XI",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
        }
        r=''
        for n in [1,4,5,9,10,40,50,90,100,400,500,900]:
            while n <= num:
                r += num_maps[n]
                num -= n
        print(r)        
    
sol = Solution()
sol.intToRoman(40)