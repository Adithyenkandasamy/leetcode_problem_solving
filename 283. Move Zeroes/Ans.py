def moveZeroes(nums):
        n = nums.count(0)
        print(n)
        for i in range(n):
            nums.remove(0)
            nums.append(0)
        print(nums)
        
li = [0,1,0,3,12]
moveZeroes(li)
