

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	
	static int N,M;
	static int[][] office;
	static ArrayList<int[]> cctvPos;
	static int[] dy = {0,0,1,-1}; //우,좌,하,상
	static int[] dx = {1,-1,0,0};
	static int[][][] cctvNum = {
			{},
			{{0},{1},{2},{3}},
			{{0,1},{2,3}},
			{{0,3},{0,2},{1,2},{1,3}},
			{{0,1,3},{0,1,2},{0,2,3},{1,2,3}},
			{{0,1,2,3}}
		};
	static ArrayList<int[][]> cctvProduct;
	static int wallCount;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		office = new int[N][M];
		cctvPos = new ArrayList<>();
		cctvProduct = new ArrayList<>();
		cctvPerm = new Stack<>();
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<M; j++){
				office[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(office[i][j]==1) {
					cctvProduct.add(cctvNum[1]);
					cctvPos.add(new int[] {i,j});
				}else if(office[i][j]==2) {
					cctvProduct.add(cctvNum[2]);
					cctvPos.add(new int[] {i,j});
				}else if(office[i][j]==3) {
					cctvProduct.add(cctvNum[3]);
					cctvPos.add(new int[] {i,j});
				}else if(office[i][j]==4) {
					cctvProduct.add(cctvNum[4]);
					cctvPos.add(new int[] {i,j});
				}else if(office[i][j]==5) {
					cctvProduct.add(cctvNum[5]);
					cctvPos.add(new int[] {i,j});
				}else if(office[i][j]==6) {
					wallCount++;
				}
				
			}
		}
		
	
		comb(0,0);
		System.out.println(N*M -(answer+wallCount+cctvPos.size()));
		
	}
	static Stack<int[]> cctvPerm;
	static int[][] temp;
	static int answer = 0;
	static void comb(int cnt, int start) {
		
		if(cnt==cctvPos.size()) {
			temp = new int[N][M];
			for(int i=0; i<N; i++) {
				for(int j=0; j<M; j++) {
					temp[i][j] = office[i][j];
				}
			}
			int sum=0;
			for(int i=0; i<cnt; i++) {
//				System.out.println(Arrays.toString(cctvPerm.get(i)));
//				System.out.println(cctvPos.get(i)[0]+" "+cctvPos.get(i)[1]);
				int result = bfs(cctvPos.get(i)[0], cctvPos.get(i)[1], cctvPerm.get(i));
//				for(int j=0; j<N; j++) {
//					System.out.println(Arrays.toString(temp[j]));
//				}
//				System.out.println(result);
				sum+=result;
				
			}
			//System.out.println("sum "+sum);
			answer = Math.max(answer, sum);
			
			return;
		}
		
		for(int[] arr: cctvProduct.get(start)) {
			cctvPerm.add(arr);
			comb(cnt+1, start+1);
			cctvPerm.pop();
			
		}	
	}
	
	static int bfs(int y, int x, int[] searchDir) {

		
		
		Queue<int[]> Q = new ArrayDeque();
		
		int monitor=0;
		for(int i: searchDir) {
			Q.add(new int[] {y,x});
			while(!Q.isEmpty()) {
				int[] arr = Q.poll();
				int a = arr[0];
				int b = arr[1];
				
				
				int ny = a +dy[i];
				int nx = b +dx[i];
				
				if(0<=ny && ny<N && 0<=nx && nx<M && temp[ny][nx]<6) {
					Q.add(new int[] {ny,nx});
					if(temp[ny][nx]==0) {
						temp[ny][nx]=-1;
						monitor++;
					}
					
				}
				
				
				
			}
		}
		
		return monitor;
	}
	
	

}
