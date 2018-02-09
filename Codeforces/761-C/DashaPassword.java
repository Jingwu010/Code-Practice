import java.util.Scanner;
import java.lang.Math;

public class DashaPassword{
	private static char[][] tokens;
	private static int[][][] scores;
	private static int rows;
	private static int cols;

	public DashaPassword(){
		initiateScores();
		dpPassword();
		System.out.println(findLargest());
	}

	private static void initiateScores(){
		scores = new int[rows][cols][8];
		for(int i = 0; i < rows; i++)
			for(int j = 0; j < cols; j++){
				int index = getTokens(tokens[i][j]);
 				for(int k = 1; k < 8; k++){
 					int[] binarys = binarifyNum(k);
 					if(binarys[index] != 1 || k ==7){
 						scores[i][j][k] = -1;
 						continue;
 					}
 					else scores[i][j][k] = Math.min(j, cols-j);
 				}
			}

		// for(int i = 0; i < rows; i++){
		// 	for(int j = 0; j < cols; j++){
		// 		for(int k = 1; k < 8; k++){
		// 			System.out.print(scores[i][j][k] + " ");
		// 		}
		// 		System.out.println("-------");
		// 	}
		// 	System.out.println();
		// }
	}

	private static void dpPassword(){
 		for(int i = 1; i < rows; i++)
 			for(int j = 0; j < cols; j++){
 				int index = getTokens(tokens[i][j]);
 				for(int k = 1; k < 8; k++){
 					int[] binarys = binarifyNum(k);
 					if(binarys[index] != 1){
 						scores[i][j][k] = -1;
 						continue;
 					}
 					System.out.println("(" + i + "," + j + "," + k + ")=" + scores[i][j][k]);
 					//System.out.println(binarys[0] + " " + binarys[1] + " " + binarys[2] + " : " + index);
 					scores[i][j][k] = compareSmaller(scores[i][j][k], binarys, i, index);
 					//System.out.println("(" + i + "," + j + "," + k + ")=" + scores[i][j][k]);
 					System.out.println("(" + i + "," + j + "," + k + ")=" + scores[i][j][k]);
 					System.out.println();
 				}
 			}
 		for(int i = 0; i < rows; i++){
			for(int j = 0; j < cols; j++){
				for(int k = 1; k < 8; k++){
					System.out.print(scores[i][j][k] + " ");
				}
				System.out.println("-------");
			}
			System.out.println();
		}
	}

	private static int compareSmaller(int step, int[] binarys, int row, int index){
		int i = row - 1;
		int mins = Integer.MAX_VALUE;
		for(int j = 0; j < cols; j++){
			for(int k = 1; k < 8; k++){
				int[] oldBinarys = binarifyNum(k);
				oldBinarys[index] = 1;
				if(scores[i][j][k] == -1) continue;
				if(checkBinarys(binarys, oldBinarys) == true){
					System.out.println("looking at " + k);
					mins = Math.min(mins, scores[i][j][k] + step);
					//System.out.println("mins = " + "(" + i + "," + j + "," + k + ")=" + mins); 
				}
			}
		}
		return step;
	}

	private static int findLargest(){
		int mins = Integer.MAX_VALUE;
		int[] standardBinary = {1, 1, 1};
		for(int i = 0; i < rows; i++)
			for(int j = 0; j < cols; j++)
				mins = Math.min(mins, scores[i][j][7]);
		return mins;
	}

	private static boolean checkBinarys(int[] b1, int[] b2){
		for(int i = 0; i < 3; i++)
			if(b1[i] != b2[i]) return false;
		return true;
	}

	private static int[] binarifyNum(int num){
		int k = num;
		int[] binarys = new int[3];
		int index = 0;
		while(k > 0){
			binarys[index] = k % 2;
			k /= 2;
			index ++;
		}
		return binarys;
	}

	private static int getTokens(char ch){
		if (ch - '0' >= 0 && ch - '0' <= 9)
    		return 0;
    	else if (ch - 'a' >= 0 && ch - 'a' <= 26)
    		return 1;
    	else if (ch == '*' || ch == '#' || ch == '&')
    		return 2;
    	return -1;
	}

	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		rows = sc.nextInt();
		cols = sc.nextInt();
		sc.nextLine();
		tokens = new char[rows][cols];
		for(int i = 0; i < rows; i++){
			StringBuffer sb = new StringBuffer(sc.nextLine());
			for(int j = 0; j < cols; j++){
				tokens[i][j] = sb.charAt(j);
			}
		}
		new DashaPassword();
	}
}