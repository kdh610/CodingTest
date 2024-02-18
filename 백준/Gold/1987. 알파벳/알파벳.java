

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	
	static int R,C;
	static char[][] board;
	static int[] dy = {0,0,1,-1};
	static int[] dx = {1,-1,0,0};
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R=Integer.parseInt(st.nextToken());
		C=Integer.parseInt(st.nextToken());
		board = new char[R][C];
		result = new Stack<>();
		alpha = new HashMap<>();
		//visit = new boolean[R][C];
		
		for(int i=0; i<R; i++) {
			board[i] = br.readLine().toCharArray();
		}
		result.add(board[0][0]);
		alpha.put(board[0][0], true);
		//visit[0][0]=true;
		
		dfs(0, 0);
		System.out.println(answer);
		
	}
	static Stack<Character> result;
	//static boolean[][] visit;
	static int answer =0;
	static Map<Character, Boolean> alpha;
	
	static void dfs(int y, int x) {
		int ny,nx;
		
		for(int i=0; i<4; i++) {
			ny = y+dy[i];
			nx = x+dx[i];
			
			if(0<=ny && ny<R && 0<=nx && nx<C) {
				
				
				if(!alpha.containsKey(board[ny][nx]) || alpha.get(board[ny][nx])==false ) {
					//visit[ny][nx] =true;
					result.add(board[ny][nx]);
					alpha.put(board[ny][nx], true);
					dfs(ny,nx);
				}
			
			}
		}
		//visit[y][x] = false;
		alpha.replace(board[y][x],false);
		answer = Math.max(answer, result.size());
		result.pop();
		
		
	}
	

}
