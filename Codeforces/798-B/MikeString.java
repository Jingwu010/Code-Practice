// 798-B

import java.util.Scanner;
import java.lang.Math;
import java.util.ArrayList;

public class MikeString{
	
	static int n;
	static int len;
	static ArrayList<Integer>[] indexes;

	private static void compareString(String first, String second, int pos){
		indexes[pos] = new ArrayList<Integer>();
		String template = first + first;
		int index = 0;

		// Looping all the indexes and record the possible index that
		// make the second string rotate into first string
		while(index < len){
			boolean flag = true;
			for(int i = 0; i < len; i++){
				if(template.charAt(i + index) != second.charAt(i)) {
					flag = false;
					break;
				}
			}
			if (flag == true){
				indexes[pos].add(index);
			}
			index ++;
		}
	}

	private static int findNearest(int pos, int cmp){
		int dis = 51;

		// find the shorest step for a given string rotate into
		// a specific form (cmp)
		for (Integer number : indexes[pos]) {
			int temDis = 0;
			if(number <= cmp) temDis = cmp - number;
			else temDis = len - number + cmp;
			if(temDis < dis)
				dis = temDis;
	   	}	
	   	return dis;
	}

	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			n = sc.nextInt();
			sc.nextLine();
			indexes = (ArrayList<Integer>[])new ArrayList[n];
			boolean flag = true;
			String first = sc.nextLine();
			len = first.length();
			indexes[0] = new ArrayList<Integer>();
			indexes[0].add(0);
			for(int i = 1; i < n; i++){
				String line = sc.nextLine();
				compareString(first, line, i);
				if(indexes[i].size() == 0) flag = false;
			}

			if(flag == false) System.out.println("-1");
			else{
				int mins = Integer.MAX_VALUE;

				// Sorting all the possible Strings derived from
				// template string (The first string) 
				for(int set = 0; set < len; set++){
					int temp = 0;
					for(int i = 0; i < n; i++){
						temp += findNearest(i, set);
					}
					mins = Math.min(mins, temp);
				}
				System.out.println(mins);
			}
		}
	}
}