class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                
nums=[2,11,15,7]
target=9

obj=Solution()
output=obj.twoSum(nums=nums,target=target)
print(output)


'''
nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self,nums,target):
        d={}
        for i in range(0,len(nums)):
            value=nums[i]
            deffernce=target-value
            if value not in d:
                d[deffernce]=i
            else:
                print(d)
                print([ d[value] , i])       

obj=Solution()
output=obj.twoSum(nums,target)

'''