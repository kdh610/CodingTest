import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int Y,X;
	static String[][] cheese;
	static Queue<int[]> Q;

	static int[] dy = {0,0,1,-1};
	static int[] dx = {1,-1,0,0};
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		Y = Integer.parseInt(st.nextToken());
		X = Integer.parseInt(st.nextToken());
		
		cheese = new String[Y][X];
		for(int i=0; i<Y; i++) {
			cheese[i] = br.readLine().split(" ");
		}
		
		
		Q = new ArrayDeque<int[]>();
		int cheeseCount = -1;
		int time = 0;
		int answer=0;
		
		while(true) {
			cheeseCount = countingDFS();
			meltDFS(0, 0);
			//System.out.println("조각 수 "+cheeseCount);
			time++;
			//System.out.println(time+"시간 후");
//			for(int i=0; i<Y; i++) {
//				System.out.println(Arrays.toString(cheese[i]));
//			}
//			System.out.println();
						
			if(cheeseCount==0) {
				break;
			}
			answer = cheeseCount;
				
		}
		
		System.out.println(time-1);
		System.out.println(answer);
		
		
	}
	
	//치즈 녹이기
	static void meltDFS(int y, int x) {
		boolean[][] visit = new boolean[Y][X];
		Q.add(new int[] {y,x});
		
		while(!Q.isEmpty()) {
			int[] yx = Q.poll();
			y = yx[0];
			x = yx[1];
			
			for(int i=0; i<4; i++) {
				int ny = y + dy[i];
				int nx = x + dx[i];
				
				if(0<=ny && ny<Y && 0<=nx && nx<X && !visit[ny][nx]) {
					visit[ny][nx] = true;
					if(cheese[ny][nx].equals("0")) {
						Q.add(new int[] {ny,nx});
					}else {
						//System.out.println("ny,nx "+ny+" "+nx);
						//System.out.println("치즈");
						cheese[ny][nx] = "0";
					}
				}
			}
		}
	}
	
	//치즈 조각 수
	static int countingDFS() {
		int cnt=0;
		boolean[][] visit = new boolean[Y][X];		
		
		for(int i=0; i<Y; i++) {
			for(int j=0; j<X; j++) {
				if(cheese[i][j].equals("1")) {
					cnt++;
				}
			}
		}
		
		return cnt;
	}
	
	

}