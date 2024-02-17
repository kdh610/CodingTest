

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

	static int N,M,D,map[][],answer;
	static int[] dy = {0,-1,0};  //왼, 위, 오
	static int[] dx = {-1,0,1};
	static Set<String> deathList;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
	
		map =new int[N][M];
		deathList = new HashSet<>();
		
		
		
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<M; j++){
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		
		for(int i=0; i<M; i++) {
			for (int j = i+1; j < M; j++) {
				for (int k = j+1; k < M; k++) {
					//System.out.println("i,j,k "+i+" "+j+" "+k);
					//맵 생성
					int [][] newMap = new int[N][M];
					for(int a=0; a<N; a++) {
						for(int b=0; b<M; b++) {
							newMap[a][b] = map[a][b];
						}
					}
					
					int sum=0;
					for(int l=0; l<N; l++) {
						//System.out.println(l+" 웨이브");
						searchEnemy(N, i, newMap);
						searchEnemy(N, j, newMap);
						searchEnemy(N, k, newMap);
						
						for(String death : deathList) {
							String[] arr = death.split(" ");
							//System.out.print(Integer.parseInt(arr[0]) + " " +Integer.parseInt(arr[1]));
							newMap[Integer.parseInt(arr[0])][Integer.parseInt(arr[1])]=0;
						}
						//System.out.println();
						//System.out.println("적수"+deathList.size());
				
						
						sum+=deathList.size();
						deathList.clear();
						enemyCharge(newMap);
						
						//적 진격후 확인
//						for(int q=0; q<N; q++) {
//							System.out.println(Arrays.toString(newMap[q]));
//						}
						
					}
					//System.out.println("======적 제것 수 ======= " + sum);
					answer = Math.max(answer,sum);
				}
				
			}
		}	
		System.out.println(answer);
	}
	
	static void enemyCharge(int[][] map) {
		
		for(int i=N-1; i>=0; i--) {
			if(i==0) {
				map[i] = new int[M]; 
				break;
			}
			map[i]=map[i-1];
		}
		
	}
	
	
	
	
	static void searchEnemy(int y, int x, int[][] map) {
		//System.out.println("서치 에너미");
		int range;
		int minDistance = 0;
		int enemyY=-1, enemyX=-1;
		int ny=0, nx=0;
		boolean enemyCheck =false;
		
		Queue<int[]> Q = new ArrayDeque<>();
		Q.add(new int[] {y,x,0});
		
		while(!Q.isEmpty()) {
			int [] yxr = Q.poll();
			y = yxr[0];
			x = yxr[1];
			range = yxr[2]+1;
			//System.out.println("y,x,range "+y+" "+x+" "+range);
			if(range>D) break;
			
			for(int i=0; i<3; i++) {
				ny = y + dy[i];
				nx = x + dx[i];
				if(0<=ny && ny<N && 0<=nx && nx<M ) {
					//System.out.println("ny,nx "+ny+" "+nx);
					if(map[ny][nx]==1) {
						//처음 적 발견 
						if(!enemyCheck) { 
							minDistance=range;
							enemyX = nx;
							enemyY = ny;
							enemyCheck=true;
							//System.out.println("처음 적 " + ny+" "+nx);
						}
						//거리가 같은데 더 오른쪽에 있다? 브레이크
						if(minDistance == range && enemyX < nx) break;
						//적이 더 왼쪽에 있다? 왼쪽적으로 갱신 
						else if(minDistance==range && enemyX > nx){
							enemyY=ny;
							enemyX =nx;
						}
						//거리가 더 늘어나면 가장 가까운 적이 아님 
						if(minDistance < range) break;
					}
					Q.add(new int[] {ny,nx,range});
				}
			}
		}
		
		if(enemyX!=-1 && enemyY!=-1)
			deathList.add(enemyY+" "+enemyX);
	}
	
	

}
