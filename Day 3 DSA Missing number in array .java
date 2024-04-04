
// Question link  - https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution


class Solution {
    int missingNumber(int array[], int n) {

        int total_expected_sum = (n * (n + 1)) / 2;
        int total_original_sum = 0;
        for (int i: array) {
            total_original_sum += i;
        }
        return total_expected_sum - total_original_sum;
    }
}

