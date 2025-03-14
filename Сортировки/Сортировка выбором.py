nums = [1, 0, -2, 5, 8]

for i in range(0, len(nums)-1):
    min_idx = i
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            min_idx = j
    if  min_idx != i:
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
print(nums)


