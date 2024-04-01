// you can find the question in this link https://www.geeksforgeeks.org/problems/count-digits5716/1

// Solution 

class Solution{
    static int evenlyDivides(int N){
        // code here
        int a = 0;
        int ans = 0;
        String temp = String.valueOf(N);
        for(int i = 0; i< temp.length(); i++){
            a = Character.getNumericValue(temp.charAt(i));
            if( a != 0 && N % a == 0){
                ans += 1;
            }
        }
        return ans;
    }
}

