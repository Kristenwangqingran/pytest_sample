#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Project :pytest_sample
@File :the sums of 2 numbers.py
@Author :jing.wang@shopee.com
@Date :22/05/2024 09:38
"""


class Solution():
    def bubbleSort(self, nums):
        """
        :param nums: List(int)
        :return:
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
        return nums

    def selectionSort(self, nums):
        for i in range(len(nums) - 1):
            min_i = i
            for j in range(i + 1, len(nums)):
                if nums[min_i] > nums[j]:
                    min_i = j
            if i != min_i:
                nums[i], nums[min_i] = nums[min_i], nums[i]

        return nums

    def merge(self, left_nums, right_nums):
        left_i = 0
        right_i = 0
        print(left_nums,right_nums)

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_nums = self.mergeSort(nums[0:mid])
        right_nums = self.mergeSort(nums[mid:])
        return self.merge(left_nums, right_nums)


nums = [7, 3, 2, 1, 8, 9, 23, 21, 6, 3, 0, 21]
s = Solution()
print(s.mergeSort(nums))
