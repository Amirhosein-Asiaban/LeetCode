"""
# Problem : Palindrome Number

## Description
Given an integer x, return true if x is a palindrome, and false otherwise.

## Approach
1. Handle negative numbers (they can't be palindromes).
2. reverse the number mathematically and compare with original.

## Complexity
- Time: O(n) 
- Space: O(1) 

## LeetCode Link
https://leetcode.com/problems/palindrome-number/

## Tags
#math #easy #palindrome

## Test Cases
Input: x = 121
Output: true

Input: x = -121  
Output: false
"""


def isPalindrome(x):
    if x < 0:
        return False
    if x < 10:
        return True
    if x % 10 == 0:  # Numbers ending with 0 (except 0) can't be palindromes
        return False
    
    original = x
    reversed_num = 0
    
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x = x // 10
    
    return original == reversed_num
