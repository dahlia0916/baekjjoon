import java.util.Scanner;
public class Main {
	
	static String tempb;
	static String kan(int n) {
		
		if (n==0){
			return "-";
		}
		StringBuilder tempb = new StringBuilder();
		for(int i=0;i<(int)(Math.pow(3, n))/3;i++) {
			 tempb.append(" ");;
		}
		return kan(n-1)+tempb+kan(n-1);

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
	
		 while (sc.hasNextInt()) {
	            int N = sc.nextInt();
	            
	            System.out.println(kan(N)); // 줄바꿈
	        }
		

	}

}
