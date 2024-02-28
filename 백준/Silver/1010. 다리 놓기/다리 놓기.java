import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int N,M;
	static int[][] dp = new int[30][30];
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		
		for(int i=0; i<30; i++) {
			for(int j=0; j<30; j++) {
				if(i==j) {
					dp[i][j]=1;
				}
				dp[i][0]=1;
			}
			//System.out.println(Arrays.toString(dp[i]));
		}
		dp[1][0]=1;
		
		
		for(int i=0; i<T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			comb(M, N);
			
//			for(int a=0; a<M+1; a++) {
//				System.out.println(Arrays.toString(dp[a])); 
//			}
			System.out.println(dp[M][N]);
		}
	}
	
	
	static int comb(int n, int r) {
		
		if(n>1 && r>=1 && n>r && dp[n][r]==0) {
			dp[n][r] = comb(n-1, r-1) + comb(n-1, r);
		}
		
		return dp[n][r];
	}
	

}