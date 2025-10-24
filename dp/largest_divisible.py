"""
    Solve : https://leetcode.com/problems/largest-divisible-subset?envType=problem-list-v2&envId=dynamic-programming
"""

nums = list(map(int , input().split()))
n = len(nums)

nums.sort()
ans = last = 0 

dp = [1] * n 
for i in range(n) :
    for j in range(i + 1 , n) : 
        if nums[j] % nums[i] == 0 :
            dp[j] = max(dp[j] , dp[i] + 1) 
            
    if ans < dp[i] : 
        last = nums[i]
        ans = dp[i]
        
# Traceback the elements
res = []
for i in range(n - 1 , -1 , -1) : 
    if dp[i] == ans and last % nums[i] == 0 :
        res.append(nums[i])
        last = res[-1]
        ans -= 1
res.reverse()
print(res)





    
        