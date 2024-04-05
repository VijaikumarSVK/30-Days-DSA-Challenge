
// Question link  - https://www.geeksforgeeks.org/problems/key-pair5616/1?itm_source=geeksforgeeks&itm_medium=Article&itm_campaign=bottom_sticky_on_Article

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

class Solution {
  boolean hasArrayTwoCandidates(int arr[], int n, int x) {
    // code here
    Arrays.sort(arr);
    int start = 0;
    int end = n - 1;

    while (start < end) {

      if (arr[start] + arr[end] == x) {
        return true;
      } else if (arr[start] + arr[end] < x) {
        start++;
      } else {
        end--;
      }
    }

    return false;
  }
}

