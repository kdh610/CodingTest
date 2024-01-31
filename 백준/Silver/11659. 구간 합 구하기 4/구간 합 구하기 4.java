import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws Exception {
		int start;
		int end;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] line = br.readLine().split(" ");
		int N = Integer.parseInt(line[0]);
		int M = Integer.parseInt(line[1]);
		
		int[] dp = new int[N+1];
		int[] nums = new int[N];
		line = br.readLine().split(" ");
		for (int i = 0; i < line.length; i++) {
			nums[i] = Integer.parseInt(line[i]);
		}
		
		dp[1] = nums[0];
		for(int i=2; i<=N; i++) {
			dp[i] = dp[i-1] + nums[i-1];
		}
		
		
		
		for(int i=0; i<M; i++) {
			int sum = 0;
			line = br.readLine().split(" ");
			
			start = Integer.parseInt(line[0]);
			end = Integer.parseInt(line[1]);
			
		
			
			System.out.println(dp[end] - dp[start-1]);
		}
		
	}

}