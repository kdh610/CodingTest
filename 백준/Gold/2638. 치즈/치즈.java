

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static int N,M;
	static int[][] map;
	static int[] dy ={1,-1,0,0};
	static int[] dx ={0,0,1,-1};
	static int time = 0;
	static int cheese = 0;
	static int sy=-1,sx=-1;
	static List<int[]> temp;
	
	public static void main(String[] args) throws Exception{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		map = new int[N][M];
		temp = new ArrayList<>();
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j =0; j<M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if(map[i][j]==0 && sy==-1 && sx==-1) {
					sy=i;
					sx=j;
					map[sy][sx]=2;
				}
				if(map[i][j]==1) cheese++;
			}
		}

		
		
		while(true) {
			//System.out.println("=========================== " + time);
			isEmpty(sy, sx);
			time++;
			
//			for(int i=0; i<N; i++) {
//				for(int j =0; j<M; j++) {
//					System.out.print(map[i][j]);
//				}
//				System.out.println();
//			}
//			System.out.println();
			
			
			for(int[] yx: temp) {
				map[yx[0]][yx[1]] = 2;	
			}
			temp.clear();
			
			
			if(cheese==0) break;
		}
		
		System.out.println(time);
		
	}
	
	static void isEmpty(int y, int x) {
		
		boolean[][] visit = new boolean[N][M];
		
		Deque<int[]> Q = new ArrayDeque<>();
		Q.add(new int[] {y,x});
		visit[y][x] = true;
		
		while(!Q.isEmpty()) {
			int[] yx = Q.pollFirst();
			y = yx[0];
			x = yx[1];
			
			if(map[y][x]==0 || map[y][x]==2 ) {
				
				for(int i=0; i<4; i++ ) {
					int ny = y + dy[i];
					int nx = x + dx[i];
					
					if(0<= ny && ny<N && 0<=nx && nx<M && !visit[ny][nx]) {
						if(map[ny][nx]!=1) {
							visit[ny][nx] = true;
//							if(ny==2 && nx==3) {
//								System.out.println("y,x " + y+" "+x);
//								System.out.println("ㅁㄴㅇㄻㄴㅇㄻㄴㅇㅇㅇㅇㅇㅇㅇㅁㅇㄹㄴㅁㅇㄹ");
//							}
							
							map[ny][nx]=2;
							
//							for(int k=0; k<N; k++) {
//								for(int j =0; j<M; j++) {
//									System.out.print(map[k][j]);
//								}
//								System.out.println();
//							}
//							System.out.println();
							
							Q.addFirst(new int[] {ny,nx});
						}else {
							Q.addLast(new int[] {ny,nx});
						}
					}
				}
			}else if(map[y][x]==1 && !visit[y][x]) {
		
				//Q.stream().map(obj -> Arrays.toString(obj)).forEach(System.out::print);
	
					melt(y,x);
					
					visit[y][x] = true; 
		
	
			}
		}
	}
	
	static void melt(int y, int x) {
		int cnt = 0;
		for(int i=0; i<4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];
			
			if(0<=ny && ny<N && 0<=nx && nx<M) {
				if(map[ny][nx] == 2) {
					//System.out.println("ny,nx" + ny + " "+nx);
					cnt++;
				} 
			}	
		}

		if(cnt>=2) {
			//System.out.println(y +" " +x);
			temp.add(new int[] {y,x});
			//System.out.println("녹음");
			cheese--;
		}
		
		
		
		
	}
	
	
	

}
