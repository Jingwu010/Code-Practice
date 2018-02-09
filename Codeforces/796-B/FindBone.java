// 796-B

import java.util.*;

public class FindBone{

	static int n, m, k;
	static Set<Integer> holes = new HashSet<Integer>();
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		while (sc.hasNext()){
			n = sc.nextInt();
			m = sc.nextInt();
			k = sc.nextInt();
			for(int i = 0; i < m; i++)
				holes.add(sc.nextInt());
			int pos = 1;
			boolean flag = true;
			for(int i = 0; i < k; i++){ 
				int from = sc.nextInt();
				int to = sc.nextInt();
				if(holes.contains(pos)){
					flag = false;
				}
				if(flag == false) continue;
				if(pos == from){
					pos = to;
				}
				else if(pos == to){
					pos = from;
				}
			}
			System.out.println(pos);
		}
	}
}