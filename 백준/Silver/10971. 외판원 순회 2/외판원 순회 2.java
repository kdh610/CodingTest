import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] cities;
	static boolean[] visit;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		cities = new int[N+1][N+1];
		
		
		for(int i=1; i<N+1; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j=1; j<N+1; j++) {
				cities[i][j] = Integer.parseInt(st.nextToken());
			}
			
		}
		
		for(int i=1; i<N+1; i++) {
			//System.out.println(i);
			visit = new boolean[N+1];
			result = new int[N];
			dfs(i, 0, i,0);
		}
		System.out.println(cost);
		
	}
	static int cost=Integer.MAX_VALUE;
	static int[] result;
	static void dfs(int first, int cnt, int start, int sum) {
		if(sum>cost) return;
		
		if(cnt==N) {
//			System.out.println(Arrays.toString(result));
//			System.out.println("cost "+sum);
//			System.out.println(Arrays.toString(visit));
			cost = Math.min(cost, sum);
			return;
		}
		
		for(int i=1; i<N+1; i++) {
			//System.out.println("start"+start+" "+i+" "+ cities[start][i]);
			if(cities[start][i]!=0) {
				if(cnt<N-1 && i==first) continue; 
				//System.out.println("i"+i);
				
				if(!visit[i]) {
					visit[i]=true;
					result[cnt]=i;
					dfs(first, cnt+1, i, sum+cities[start][i]);
					visit[i]=false;
				}
			}
		}
		
		
		
		
	}
	
	
	
}