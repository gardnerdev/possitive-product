# Subarrays algorithm

Given an list arr consisting of N integers `-1` or `1` the task is to print the length of the longest subarray with a product equal 1

Examples:
```
    Input: arr =[1, -1, -1, 1, 1, -1]
    Output: 5
    Explanation:
    The longest subarray with positive products is: {1, -1, -1, 1, 1}. 
    Therefore, the required length is 5.

    Input: arr=[1, -1, -1, -1, 1, 1]
    Output: 4
    Explanation:
    The longest subarray with positive products are: {-1, -1, -1, 1}. 
    Therefore, the required length is 4.
```

**Naive Approach**: The simplest approach to solve the problem is to generate all possible subarrays and check if its product is `1`or `-1`. Among all such subarrays, print the length of the longest subarray obtained.
**Time Complexity**: (N^{3})
**Auxiliary Space**: O(1)
Efficient Approach: The problem can be solved using **Dynamic Programming**. 
The idea here is to maintain the count of `1` elements and `-1` elements such that their product is positive.

* Initialize the variable, say res, to store the length of the longest subarray with the positive product.
* Initialize two variables, **Pos** and **Neg**, to store the length of the current subarray with the positive and negative products respectively.
* Iterate over the array.
* If arr[i] = 0: Reset the value of **Pos** and **Neg**.
* If arr[i] == 1: Increment **Pos** by 1. If at least one element is present in the subarray with the negative product, then increment **Neg** by 1.
If arr[i] == -1: Swap **Pos** and **Neg** and increment the **Neg** by 1. 
If at least one element is present in the subarray with the positive product, then increment **Pos** also.
Update res=max(res, Pos).