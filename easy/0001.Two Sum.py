"""
## Problem : Two Sum

## Description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

## Approach
Used a hash map to store numbers and their indices.

## Complexity
- Time: O(n)
- Space: O(n)

## LeetCode Link
https://leetcode.com/problems/two-sum/

## Tags
#array #hash-table #easy

## Test Cases
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

