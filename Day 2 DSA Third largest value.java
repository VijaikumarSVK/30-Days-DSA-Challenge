// you can find the question in this link - https://www.geeksforgeeks.org/problems/third-largest-element/1

// solution 

class Solution
{
    int thirdLargest(int a[], int n)
    {
	    // Your code here
        int ans = 0;
        int first_largest = a[0];
        int second_largest = 0;
        int third_largest = 0;
        int temp = 0;
        
        if(a.length < 3){
            ans = -1;
        }else{
            for( int i = 1; i <a.length ; i++){
                if(a[i] > first_largest){
                    temp = first_largest;
                    first_largest = a[i];
                    third_largest = second_largest;
                    second_largest = temp;
                }else if(a[i] > second_largest){
                    third_largest = second_largest;
                    second_largest = a[i];
                }else if(a[i]> third_largest){
                    third_largest = a[i];
                }
                temp = 0;
            }
           ans = third_largest ;
        }
    return ans;
    }   
}