
// Question link  - https://www.geeksforgeeks.org/problems/wave-array-1587115621/1?page=2&category=Arrays&sortBy=submissions

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

class Solution {
  public static void convertToWave(int n, int[] a) {
    // code here
    if (n % 2 == 0) {
      n = n;
    } else {
      n = n - 2;
    }
    for (int i = 0; i < n; i += 2) {
      int temp = a[i];
      a[i] = a[i + 1];
      a[i + 1] = temp;
    }
  }
}


