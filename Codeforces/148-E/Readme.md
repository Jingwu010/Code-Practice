### 148/E Procelain

#### 1. Abstract:

​	A shelf has #**n** rows , each row contains #**k** procelains with different values and they are well placed from left to right. Each time we want to take off a procelain with maximum value in the outer side of the shelf (leftmost and rightmost in each row). Question is the maximum value we can get after taking #**m** porcelains.



#### 2. Samples

~~~~
input
  2 3
  3 3 7 2
  3 4 1 5
output
  15
	
input
  1 3
  4 4 3 1 2
output
  9
~~~~



#### 3. Idea

​	The general idea of solving this problem is dynamic programming. 

​	Each dp[i, j] means the maximum value we get so far from row 1 to row i with j porcelains available. While initializing dp[i, j] to be the maximum value we can get at row i with j porcelains. Before starting, each value in dp (in each row) is totally indenpendent of others.

​	The reason we can use dynamic programming is for each row, with j items available, we can view it as a combination k items in current row and j-k items from above rows. As a result, dp[i, j] always ends up with the max value we can get from the i rows above with j items.

​	The transition equation should look like:

​		`dp[i][j] = Maxof(dp[i][k] + dp[i-1][j - k])`



#### 4. Pitfalls and Tips

- Use prefixValue to cut down complexity when initilazing dp matrix
- Consider the boundary of dp loop
  - For initialization, we only need loop j from 0 to Minof(len, m)
  - For searching maximum value in dp, we only need loop k from 0 to min(j, len), which means each row can contribute at most #len items into maximum value



#### 5. Algorithm Complexity 

+ For initialization of dp matrix — O(n ^ 3)
+ For calculation of dp matrix — O(n ^ 2 * m)



#### 6. Core blocks

~~~~java
// Init dp[][]
for(int i = 1; i <= n; i++){
    int col = valueTable[i].length - 1;
    // For each row, the dp[i] length is Min(col, m) when initialized
    for(int j = 1; j <= Math.min(col, m); j++){
        int mins = -1;
        for(int k = 0; k <= j; k++){
            mins = Math.max(mins, prefixValue[i][k] + 
                        prefixValue[i][col] - prefixValue[i][col - (j - k)]);
        }
        dp[i][j] = mins;
    }
}
~~~~



~~~~java
// Loop dp[][] from 0 - i and 0 - m
int colSum = 0;
for(int i = 1; i <= n; i ++){
    // Open a new array to store the dp value
    int[] newDp = new int[m+1];
    colSum += valueTable[i].length;
    // For each row, the dp[i] length is Min(colSum, m)
    // Cause the number of items so far could only contribute to # of colSum
    // Beyond that, we can assume there is no effect
    for(int j = 0; j <= Math.min(m, colSum); j++){
        int mins = -1;
        // In each row, we can use from 1 to # of Min(m, len)
        // of items maxValue to update dp[i][j]
        for(int k = 0; k <= Math.min(j, valueTable[i].length); k++){
            mins = Math.max(mins, dp[i][k] + dp[i-1][j - k]);
        }
        newDp[j] = mins;
    }
    dp[i] = newDp;
}
return dp[n][m];
~~~~

