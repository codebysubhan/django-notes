k = int(input().strip())
nums = list(map(int, input().strip().split()))

stop = False
for i in range(len(nums)):
    for j in range(i, len(nums)+1):
        if sum(nums[i:j]) == k:
            print(nums[i:j])
            stop = True
            break
    if stop:
        break


# i = 0
# j = 1
#
# chk = nums[i]
# found = False
# while i < len(nums) and j < len(nums):
#     if chk < k:
#         chk += nums[j]
#         j += 1
#     elif chk == k:
#         print(nums[i:j])
#         found = True
#         break
#     elif chk > k:
#         chk -= nums[i]
#         i += 1
#
# if not found:
#     print('not present')
