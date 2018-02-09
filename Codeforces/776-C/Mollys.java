import java.util.*;
import java.util.Scanner;
import java.lang.Math;
public class Mollys{

	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			int n = sc.nextInt();
			int k = sc.nextInt();
			long upperBound = 0;
			int[] values = new int[n];
			long[] prefix = new long[n];
			for(int i = 0; i < n; i++){
				values[i] = sc.nextInt();
				prefix[i] = (i == 0 ? 0 : prefix[i-1]) + values[i];
				upperBound += Math.abs(values[i]);
			}
			int ans = 0;
			int interval = 1;
			while(interval <= upperBound){
				Map<Long, Integer> map = new HashMap<Long, Integer>();
				map.put(0l, 1);
				for(int i = 0; i < n; i++){
					if (map.get(prefix[i]) != null){
						ans += map.get(prefix[i]);
						int tmp = map.get(prefix[i]);
						map.remove(prefix[i]);
						map.put(prefix[i], tmp + 1);
					}
					//System.out.println(prefix[i] + " hit " + interval);
					else map.put(prefix[i], 1);
				}
				interval *= k;
				if(interval == 1) break; //if k = 1 or k = -1
			}
			System.out.println(ans);
		}
	}
}