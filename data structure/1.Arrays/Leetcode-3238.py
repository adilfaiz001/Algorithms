class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxWindow = 0
        currentWindow = 0
        start = -1

        for index, value in enumerate(nums):
            if value == 1 and start == -1:
                start = index
            elif value == 0 and start != -1:
                currentWindow = index - start
                start = -1

                if(currentWindow > maxWindow):
                    maxWindow = currentWindow

        if(start != -1):
            currentWindow = len(nums) - start
            if(currentWindow > maxWindow):
                    maxWindow = currentWindow

        return maxWindow

sol = Solution();
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]));
# result = sol.findMaxConsecutiveOnes([1,0,1,1,0,1])
# print(result)