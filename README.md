# 2016. Maximum Difference Between Increasing Elements

Given a 0-indexed integer array nums of size n, find the maximum difference between </br>
nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j]. </br>

Return the maximum difference. If no such i and j exists, return -1. </br>

## Example 1:

Input: nums = [7,1,5,4] </br>
Output: 4 </br>
Explanation: </br>
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4. </br>
Note that with i = 1 and j = 0,  </br>
the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid. </br>

## Example 2:

Input: nums = [9,4,3,2] </br>
Output: -1 </br>
Explanation: </br>
There is no i and j such that i < j and nums[i] < nums[j]. </br>

## Example 3:

Input: nums = [1,5,2,10] </br>
Output: 9 </br>
Explanation: </br>
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9. </br>

## Constraints:

n == nums.length </br>
2 <= n <= 1000 </br>
1 <= nums[i] <= 109 </br>
