class Solution:
    def getConcatenation(self, nums):
        result = []

        for num in nums:
            result.append(num)

        for num in nums:
            result.append(num)

        return result
    
    
    
    #class Solution:
    #def getConcatenation(self, nums: List[int]) -> List[int]:
        #ans=nums+nums
        #return ans