import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N,M;
	static int[] result;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		result = new int[M];
		
		
		comb(0,1);
		
		
	}
	
	private static void comb(int count, int start) {
		if(count==M) {
			for (int i : result) {
				System.out.print(i+" ");
			}
			System.out.println();
			return;
		}
		
		for(int i=start; i<=N; i++) {
			result[count] = i;
			comb(count+1,i+1);
			
		}
		
		
	}

}