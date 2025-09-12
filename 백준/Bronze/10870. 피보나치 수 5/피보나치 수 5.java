import java.util.Scanner;
public class Main {
	
	static int fib(int n) {
		if(n<=1){
			return n;
		}
		else {
			return fib(n-1)+fib(n-2);
		}
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		System.out.println(fib(N));
	
		
		

	}

}
