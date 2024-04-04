import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	static int N,L,answer=0;
	static int[][] map;
	static boolean[] row,col;
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
		map = new int[N][N];
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		//System.out.println("==================행");
		count(map);
		map = rotate(map);	
		//System.out.println("==================열");
		count(map);
		System.out.println(answer);
	}
	
	static void count(int[][] map) {
		for (int i = 0; i < N; i++) {
			//System.out.println("============i : "+i);
			boolean possible = true;
			boolean[] check = new boolean[N];
			int length = 1;
			int prev = map[i][0];
			for (int j = 1; j < N; j++) {
				//System.out.println("j "+j);
				
				if(Math.abs(map[i][j]-prev)>=2) {
					possible=false;
					break;
				}
				//오르막
				if(prev<map[i][j]) {
					//경사로 놓을 자리, 경사로가 이미 있는지 체크 
					//System.out.println("오르막");
					//System.out.println(Arrays.toString(check));
					if(j-L<0 || !isFlat(j-L, j, map[i]) || isSlope(j-L, j, check)) {
						//System.out.println("오르막 불가");
						possible =false;
						break;
					}
				}
				//내리막
				else if(prev > map[i][j]) {
					//경사로 놓을 자리 
					//System.out.println("내리막");
					
					if(j+L-1>=N || !isFlat(j, j+L, map[i])) {
						//System.out.println("내리막 불가");
						possible=false;
						break;
					}
					
					for(int k=j; k<j+L; k++) {
						check[k]=true;
					}
				}
				prev = map[i][j];
			}
			if(possible) {
				//System.out.println(i+"행 가능");
				answer++;
			}
		}
	}
	
	
	
	static int[][] rotate(int[][] map){
		int[][] arr = new int[N][N];
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				arr[i][j] = map[j][i];
			}
		}
		
		return arr;
	}
	
	
	
	static boolean isSlope(int start, int end, boolean[] slope) {
		for (int i = start; i < end; i++) {
			if(slope[i]) {
				return true;
			}
		}
		return false;
	}
	
	
	
	static boolean isFlat(int start, int end, int[] map) {
		boolean flag = true;
		int height = -1;
		for(int i=start; i<end; i++) {
			if(height==-1) {
				height=map[i];
				continue;
			}
			if(height!=map[i]) {
				flag = false;
				break;
			}
		}
		return flag;
	}

}