
// Question link  -https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

// youtube link - https://www.youtube.com/c/https:/www.youtube.com/@encodecode1

// Solution

class Solution {
  public int maxProfit(int[] prices) {
    int min_price = Integer.MAX_VALUE;
    int max_profit = 0;

    for (int price: prices) {
      if (price < min_price) {
        min_price = price;
      } else if (price - min_price > max_profit) {
        max_profit = price - min_price;
      }
    }
    return max_profit;
  }
}	
