
// Question link  - https://www.geeksforgeeks.org/problems/jump-game/1

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

class Solution {
  static int canReach(int[] A, int N) {
    // code here
    int r = 0;

    for (int i = 0; i < N; i++) {
      if (r < i) {
        return 0;
      }
      r = Math.max(r, i + A[i]);
    }
    return 1;
  }
};

