"""
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

示例 1：

输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。

"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = 0

        res_list = []
        for num in nums:
            count += num
            res_list.append(count)

        return res_list
