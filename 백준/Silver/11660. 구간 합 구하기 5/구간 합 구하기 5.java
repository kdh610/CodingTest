import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws Exception {
		int start;
		int end;
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sb = new StringBuffer();
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[][] table = new int[N+1][N+1];
		int[][] dp = new int[N+1][N+1];
		
		
		
		for(int i=1; i<N+1; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=1; j<N+1; j++) {
				table[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		
		for(int i=1; i<N+1; i++) {
			dp[i][1] = table[i][1];
		}
		
		for(int i=1; i<N+1; i++) {
			for(int j=1; j<N+1; j++) {
				dp[i][j] = dp[i][j-1] + table[i][j];
			}
		}
		
		for(int i=2; i<N+1; i++) {
			for(int j=1; j<N+1; j++) {
				dp[i][j] += dp[i-1][j]; 
			}
			
		}
		
		
		
		
		for(int i=0; i<M; i++) {
			int sum =0;
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			
			sum = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1];
			
			
			sb.append(sum);
			sb.append("\n");
//			System.out.println(sum);
			
			
		}
		
		System.out.println(sb.toString());
		
		
	}

}