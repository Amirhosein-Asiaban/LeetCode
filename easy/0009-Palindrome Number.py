"""
# Problem : Palindrome Number

## Description
Given an integer x, return true if x is a palindrome, and false otherwise.

## Approach
1. Handle negative numbers and numbers ending with 0 (except 0).
2. Reverse only half of the number and compare with the other half.
3. This avoids integer overflow and is more efficient.

## Complexity
- Time: O(log₁₀(n)) - where n is the number of digits
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
    
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Numbers ending with 0 (except 0) can't be palindromes
    if x % 10 == 0 and x != 0:
        return False
    
    reversed_half = 0
    
    # Reverse only half of the number
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # For even digits: x == reversed_half
    # For odd digits: x == reversed_half // 10
    return x == reversed_half or x == reversed_half // 10
