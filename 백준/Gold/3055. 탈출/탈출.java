

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int R,C;
	static String[][] map;
	static ArrayList<int[]> water;
	
	static int[] gosoom,beaver;
	static int time;
	static int[] dy = {0,0,1,-1};
	static int[] dx = {1,-1,0,0};
	static boolean possible;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		map = new String[R][C];
		
		for(int i=0; i<R; i++) {
			map[i] = br.readLine().split("");
		}
		
		water = new ArrayList<>();
		gosoom = new int[2];
		beaver = new int[2];
		
		for(int i=0; i<R; i++) {
			for(int j=0; j<C; j++) {
				if(map[i][j].equals("*")) {
					water.add(new int[] {i,j});
				}else if(map[i][j].equals("S")) {
					gosoom[0]=i;
					gosoom[1]=j;
					map[i][j] = "0";
				}else if(map[i][j].equals("D")) {
					beaver[0] = i;
					beaver[1] = j;
				}
			}
		}
		
		Queue<int[]> Q = new ArrayDeque<int[]>();
		
		Q.add(new int[] {gosoom[0],gosoom[1]});
		for(int[] w: water) {
			Q.add(new int[] {w[0],w[1]});			
		}
		
		while(!Q.isEmpty()) {

			int[] yx = Q.poll();
			int y = yx[0];
			int x = yx[1];
			
			if(map[beaver[0]][beaver[1]].equals("*") || map[beaver[0]][beaver[1]].chars().allMatch(Character::isDigit)) {
				break;
			}
			
			
			for(int i=0; i<4; i++) {
				int ny = y + dy[i];
				int nx = x + dx[i];
				if(0<=ny && ny<R && 0<=nx && nx<C) {
					if(map[y][x].chars().allMatch(Character::isDigit)) {
						if(map[ny][nx].equals(".") || map[ny][nx].equals("D")) {
							map[ny][nx] = (Integer.parseInt(map[y][x]) + 1)+"";
							Q.add(new int[] {ny,nx});
						}
					}
					if(map[y][x].equals("*")) {
						if(map[ny][nx].equals(".") || map[ny][nx].chars().allMatch(Character::isDigit)) {
							map[ny][nx] = "*";
							Q.add(new int[] {ny,nx});
						}
					}
					
				}
			}
			
		}
		
		if(map[beaver[0]][beaver[1]].equals("D"))  System.out.println("KAKTUS");
		else System.out.println(map[beaver[0]][beaver[1]]);
		
	}
	
	

	

}