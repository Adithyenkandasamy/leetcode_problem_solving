val = 3
nums = [2,3,2]
nums.sort()
# print(nums)
c_o_v = nums.count(val)
for i in range(c_o_v):
    nums.remove(val)
print(nums,c_o_v)    