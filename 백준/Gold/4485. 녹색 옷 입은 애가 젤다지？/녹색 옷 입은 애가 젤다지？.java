

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[] dy = {0,0,1,-1};
	static int[] dx = {1,-1,0,0};

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc=0;
		
		while(true) {
			tc++;
			int N = Integer.parseInt(br.readLine());
			
			if(N==0) break;
			
			int[][] cave = new int[N][N];
			int[][] temp = new int[N][N];
			
			
			for(int i=0; i<N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for(int j=0; j<N; j++) {
					cave[i][j]= Integer.parseInt(st.nextToken());
				}
			}
			
			for(int i=0; i<N; i++) {
				Arrays.fill(temp[i], Integer.MAX_VALUE);
			}
			temp[0][0] = cave[0][0];
			
			
			Queue<int[]> Q = new ArrayDeque<>();
			
			Q.add(new int[] {0,0});
		
			
			while(!Q.isEmpty()) {
				
				int[] yx = Q.poll();
				int y = yx[0];
				int x = yx[1];
				
				for(int i=0; i<4; i++) {
					int ny = y + dy[i];
					int nx = x + dx[i];
					
					if(0<=ny && ny<N && 0<=nx && nx<N) {
						if(temp[ny][nx] > temp[y][x] + cave[ny][nx]) {
									
							temp[ny][nx] = temp[y][x] + cave[ny][nx];
							Q.add(new int[] {ny,nx});
						}
			

					}
				}
			}
			
			System.out.println("Problem "+tc+":"+" "+temp[N-1][N-1]);
			
		}
		
		
		
	}
}
