#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags:
## Description:
##     https://leetcode.com/problems/string-compression/description/
##    ,-----------
##    | Given an array of characters, compress it in-place.
##    | 
##    | The length after compression must always be smaller than or equal to the original array.
##    | 
##    | Every element of the array should be a character (not int) of length 1.
##    | 
##    | After you are done modifying the input array in-place, return the new length of the array.
##    | 
##    | 
##    | Follow up:
##    | Could you solve it using only O(1) extra space?
##    | 
##    | 
##    | Example 1:
##    | Input:
##    | ["a","a","b","b","c","c","c"]
##    | 
##    | Output:
##    | Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
##    | 
##    | Explanation:
##    | "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
##    | Example 2:
##    | Input:
##    | ["a"]
##    | 
##    | Output:
##    | Return 1, and the first 1 characters of the input array should be: ["a"]
##    | 
##    | Explanation:
##    | Nothing is replaced.
##    | Example 3:
##    | Input:
##    | ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
##    | 
##    | Output:
##    | Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
##    | 
##    | Explanation:
##    | Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
##    | Notice each digit has it's own entry in the array.
##    | Note:
##    | All characters have an ASCII value in [35, 126].
##    | 1 <= len(chars) <= 1000.
##    `-----------
##
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ## Idea: sqrt(num)
        ## Complexity:
        ## Sample Data:
        ##    1 2 7
        if num <= 1:
            return False
        import math
        sum = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                sum += i
                if i != num/i:
                    sum += num/i
        return sum == num