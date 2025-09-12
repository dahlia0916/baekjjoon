import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
	static int  N;
	static int tc;
	static ArrayList<int[]> input = new ArrayList<>();
	static int[][] numbers;
	static ArrayList<Integer> ans = new ArrayList<>();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N=sc.nextInt();
		
		numbers  = new int[N][2];
		
		for(int i=0;i<N;i++) {
			int x = sc.nextInt();
            int y = sc.nextInt();
            input.add(new int[]{x, y});
		
		}
		subset(0,0);
		System.out.println(Collections.min(ans));

	}
	
	private static void subset(int depth,int len) {
		
		
		if(depth == N) {
			tc++;
			int sour=1;
			int bitter=0;
			for(int i=0;i<len;i++) {
				sour=sour*numbers[i][0];
				bitter=bitter+numbers[i][1];
			}
			if(len>0) {
				ans.add(Math.abs(sour-bitter));
			}

			
			return ;
		}
		
		numbers[len][0]=input.get(depth)[0];
		numbers[len][1]=input.get(depth)[1];
		subset(depth+1,len+1);
		subset(depth+1,len);
		
	}
	

}
