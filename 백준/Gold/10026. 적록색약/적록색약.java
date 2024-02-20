import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;

public class Main {

	static int N;
	static char[][] picture;
	static int[] normal;
	static int[] colorBlind;
	static Queue<int[]> Q;
	static int[] dy= {0,0,1,-1};
	static int[] dx= {1,-1,0,0};
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N= Integer.parseInt(br.readLine());
		picture = new char[N][N];
		
		
		for(int i=0; i<N; i++) {
			picture[i] = br.readLine().toCharArray();
		}
		
		normal = new int[] {0,0,0};
		colorBlind = new int[] {0,0,0};
		
		boolean[][] visit = new boolean[N][N];
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if(visit[i][j]) continue;
				
				Q= new ArrayDeque<>();
				
				Q.add(new int[] {i,j});
				
				char cur = picture[i][j];
				visit[i][j] = true;
				
				if(cur=='R') {
					normal[0]+=1;
					picture[i][j] = 'G';
				}
				else if(cur=='G') normal[1]+=1;
				else normal[2]+=1;
				
				
				while(!Q.isEmpty()) {
					int[] yx = Q.poll();
					
					int y = yx[0];
					int x = yx[1];
					
					for(int k=0; k<4; k++) {
						int ny = y+dy[k];
						int nx = x+dx[k];
						
						if(0<=ny && ny<N && 0<=nx && nx<N) {
							if(picture[ny][nx]==cur && !visit[ny][nx]) {
								visit[ny][nx] = true;
								if(cur=='R' && picture[ny][nx]=='R') {
									picture[ny][nx] = 'G';
								}
								Q.add(new int[] {ny,nx});
							}
						}
					}
				}
			}
		}
		
		
		visit = new boolean[N][N];
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if(visit[i][j]) continue;
				
				visit[i][j] = true;
				char cur = picture[i][j];
				Q= new ArrayDeque<>();
				
				Q.add(new int[] {i,j});
				
				if(cur=='R') {
					colorBlind[0]+=1;
				}
				else if(cur=='G') colorBlind[1]+=1;
				else colorBlind[2]+=1;
				
				while(!Q.isEmpty()) {
					int[] yx = Q.poll();
					int y = yx[0];
					int x = yx[1];
					for(int k=0; k<4; k++) {
						int ny = y+dy[k];
						int nx = x+dx[k];
						
						if(0<=ny && ny<N && 0<=nx && nx<N) {
							if(!visit[ny][nx] && picture[ny][nx]==cur) {
								visit[ny][nx] = true;
								Q.add(new int[] {ny,nx});
							}
						}
						
					}
					
				}
			}
		}
	
		int sum1=0, sum2=0;
		
		for(int i=0; i<3; i++) {
			sum1+=normal[i];
			sum2+=colorBlind[i];
		}
		
		System.out.println(sum1+" "+sum2);
	}

}