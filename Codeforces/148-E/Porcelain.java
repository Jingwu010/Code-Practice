import java.util.Scanner;
import java.lang.Math;
public class Porcelain{

	/*
	 *	dp[i][j] means the maximum value we got so far
	 *	from 0 to row i, with j porcelains
	 */
	private int[][] dp;

	/*
	 *	prefixValue[i][j] means the prefix sum of
	 *	j numbers at row i
	 */
	private int[][] prefixValue;

	public Porcelain(int n, int m, int[][] valueTable){
		dp = new int[n+1][m+1];
		init(n, m, valueTable);
		System.out.println(calculate(n, m, valueTable));
	}

	/*
	 *	initiate dp value to be the maximum value
	 *	at row i, with j procelains
	 */
	private void init(int n, int m, int[][] valueTable){
		
		// Init prefixValue[][]
		prefixValue = valueTable;
		for(int i = 1; i <= n; i++){
			for(int j = 1; j < valueTable[i].length; j++){
				prefixValue[i][j] = prefixValue[i][j-1] + valueTable[i][j];
			}
		} 

		
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
	}

	private int calculate(int n, int m, int[][] valueTable){
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
	}

	private static void showMatrix(int[][] matrix){
		for(int i = 1; i < matrix.length; i++){
			for(int j = 0; j < matrix[i].length; j++)
				System.out.print(matrix[i][j] + " ");
			System.out.println();
		}
	}

	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			int n = sc.nextInt();
			int m = sc.nextInt();
			int[][] valueTable = new int[n+1][];
			valueTable[0] = new int[0];
			for(int i = 1; i <= n; i++){
				int col = sc.nextInt();
				valueTable[i] = new int[col+1];
				for(int j = 1; j <= col; j++)
					valueTable[i][j] = sc.nextInt();
			}
			Porcelain por = new Porcelain(n, m, valueTable);
		}
		sc.close();
	}
}
