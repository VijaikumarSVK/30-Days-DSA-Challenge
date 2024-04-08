
// Question link  - https://leetcode.com/problems/two-sum/submissions/1226319684/

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

class Solution {
  public int[] twoSum(int[] nums, int target) {
    int return_arr[] = new int[2];
    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] + nums[j] == target) {
          return_arr[0] = i;
          return_arr[1] = j;
        }
      }
    }
    return return_arr;
  }
}
