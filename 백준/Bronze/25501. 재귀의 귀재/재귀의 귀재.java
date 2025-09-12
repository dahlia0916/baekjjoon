import java.util.ArrayList;
import java.util.Scanner;
public class Main {
	static int count=0;
	static ArrayList<Integer> count_l = new ArrayList<>();

	static int rec(String s, int l, int r,int count) {
		if(l>=r) {
			count_l.add(count+1);
			return 1;
		}
		if(s.charAt(l)!=s.charAt(r)) {
			count_l.add(count+1);
			return 0;
		}
		return rec(s,l+1,r-1,count+1);
	}
	
	static int pal(String s) {
		return rec(s,0,s.length()-1,0);
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		sc.nextLine();
		for (int i=0;i<N;i++) {
			String S = sc.nextLine();
			if(pal(S)==1) {
				
				System.out.println("1 "+count_l.get(i));
			}
			else {
				String temp="";
				temp.concat("0 ");
				temp.concat(Integer.toString(count));
				System.out.println("0 "+count_l.get(i));
			}
		}
	
	}

}
