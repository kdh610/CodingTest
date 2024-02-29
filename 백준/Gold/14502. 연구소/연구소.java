import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N,M;
	static int[][] map;
	static int wall=3;
	static ArrayList<int[]> virus, space;
	static int wY1,wX1, wY2,wX2, wY3,wX3;
	static int[] dy = {0,0,1,-1};
	static int[] dx = {1,-1,0,0};
	static int max=0;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N=Integer.parseInt(st.nextToken());
		M=Integer.parseInt(st.nextToken());
		map = new int[N][M];
		virus = new ArrayList<>();
		space = new ArrayList<>();
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<M; j++) {
				int a = Integer.parseInt(st.nextToken());
				map[i][j] = a;
				if(a==1) wall++;
				else if(a==2) virus.add(new int[] {i,j});
				else space.add(new int[] {i,j});
			}
		}
		
		for(int i=0; i<space.size(); i++) {
			wY1 = space.get(i)[0];
			wX1 = space.get(i)[1];
			
			for(int j=i+1; j<space.size(); j++) {
				wY2 = space.get(j)[0];
				wX2 = space.get(j)[1];
				for(int k=j+1; k<space.size(); k++) {
					wY3 = space.get(k)[0];
					wX3 = space.get(k)[1];
					
					int[][] newMap = refreshMap();
					newMap[wY1][wX1] = 1;
					newMap[wY2][wX2] = 1;
					newMap[wY3][wX3] = 1;
					
					int result = bfs(newMap);
					max = Math.max(max, result);
				}
			}
		}
		System.out.println(max);
		
	}
	
	
	static int bfs(int[][] newMap) {
		Queue<int[]> q = new ArrayDeque<int[]>();
		for(int[] v: virus) {
			q.add(v);
		}
		int cnt=virus.size();
		
		while(!q.isEmpty()) {
			int[] yx = q.poll();
			
			for(int i=0; i<4; i++) {
				int ny = yx[0] + dy[i];
				int nx = yx[1] + dx[i];
				
				if(0<=ny && ny<N && 0<=nx && nx<M && newMap[ny][nx]==0) {
					newMap[ny][nx] = 2;
					cnt++;
					q.add(new int[] {ny,nx});
				}
				
			}
		}
		
		return (N*M) - wall - cnt;
	}
	
	
	
	
	static int[][] refreshMap(){
		int[][] newMap = new int[N][M];
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				newMap[i][j] = map[i][j];
			}
		}
		return newMap;
	}
	

	
	
}