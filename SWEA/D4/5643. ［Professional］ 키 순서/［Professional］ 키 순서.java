

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static int N,M;
	static int INF = (int)1e9;

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int T= Integer.parseInt(br.readLine());
		
		for(int test_case = 1; test_case <= T; test_case++){
			StringTokenizer st;
			
			N = Integer.parseInt(br.readLine());
			M = Integer.parseInt(br.readLine());
			
			
			int[][] graph = new int[N+1][N+1];
			for (int i = 1; i < N+1; i++) {
				Arrays.fill(graph[i], INF);
			}
			
			for(int i=0; i<N+1; i++) {
				for(int j=0; j<N+1; j++) {
					if(i==j) graph[i][j]=0;
				}
			}
			
			
			for(int i=0; i<M; i++) {
				st = new StringTokenizer(br.readLine());
				int start = Integer.parseInt(st.nextToken());
				int end = Integer.parseInt(st.nextToken());
				graph[start][end]=1;
			}
			
			
			
			for(int k=1; k<N+1; k++ ) {
				for(int a=1; a<N+1; a++ ) {
					for(int b=1; b<N+1; b++ ) {
						graph[a][b] = Math.min(graph[a][b], graph[a][k]+graph[k][b]);
					}
				}
			}
			
			
			int answer=0;
			for(int i=1; i<N+1; i++) {
				int cnt=0;
				for(int j=1; j<N+1; j++) {
					if(graph[i][j]!=0 && graph[i][j]!=INF) {
						cnt++;
					}
					if(graph[j][i]!=0 && graph[j][i]!=INF) {
						cnt++;
					}
				}
				if(cnt==N-1) answer++;
			}
			
			System.out.println("#"+test_case+" "+answer );


		}
		
		
		
		
	}

}
