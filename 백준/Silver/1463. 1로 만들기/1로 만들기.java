import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int[][] dp = new int[N+1][3];
		
		for(int i=2; i<N+1; i++) {
			Arrays.fill(dp[i], Integer.MAX_VALUE);
		}
		
		
		
		for(int i=2; i<N+1; i++) {
			if(i%3==0) {
				dp[i][0]= Math.min(Math.min(dp[i/3][0],dp[i/3][1]), dp[i/3][2]) +1; 
			}
			if(i%2==0) {
				dp[i][1]= Math.min(Math.min(dp[i/2][0],dp[i/2][1]), dp[i/2][2]) +1;
			}
			
			dp[i][2]= Math.min(Math.min(dp[i-1][0],dp[i-1][1]), dp[i-1][2]) +1;
		}
		
//		for(int i=1; i<N+1; i++) {
//			System.out.println(Arrays.toString(dp[i]));
//			
//		}
		
		System.out.println(Math.min(Math.min(dp[N][0], dp[N][1]), dp[N][2]));
		
	}

}