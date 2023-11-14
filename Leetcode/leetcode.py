def numberOfSubarrays(self, nums, k):
    i=0
    j=0
    count=0
    ans=0
    while(i<len(nums)):
        if nums[i]%2==1:
            count+=1
        if count==k:
            temp=i
            while(i<len(nums) and nums[i]%2==0):
                i+=1
            left=i-temp
            while(i<len(nums) and nums[i]%2==1):
                i+=1
            right=i-temp
            ans+=left*right
            count-=1
        else:
            i+=1