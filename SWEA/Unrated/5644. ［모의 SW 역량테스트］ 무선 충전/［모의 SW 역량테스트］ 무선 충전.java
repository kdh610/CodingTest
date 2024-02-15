
import java.util.Scanner;
import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
    	static int M,A; //총 이동시간, BC의 개수
	static String[] AmoveInfo, BmoveInfo;
	static String[][] map;
	static ArrayList<Bc> bcList;
	static PriorityQueue<Integer> maxPower;
	// 1좌, 2하, 3우, 4상
	static int[] dy = {0,0,1,0,-1 };
	static int[] dx = {0,-1,0,1,0};
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T;
		T=Integer.parseInt(br.readLine());

		for(int test_case = 1; test_case <= T; test_case++)
		{
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		M=Integer.parseInt(st.nextToken());
		A=Integer.parseInt(st.nextToken());
		AmoveInfo = new String[M];
		BmoveInfo = new String[M];
		String a = "0 "+br.readLine();
		String b = "0 "+br.readLine();
		AmoveInfo = a.split(" ");
		BmoveInfo = b.split(" ");
		
		

		bcList = new ArrayList<>();
		
		for(int i=0; i<A; i++) {
			st = new StringTokenizer(br.readLine());
			
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int p = Integer.parseInt(st.nextToken());

			Bc bc = new Bc(x-1,y-1,c,p);
			bcList.add(bc);
			
		}
		
		
		
		User userA = new User(0,0);
		User userB = new User(9,9);
		maxPower = new PriorityQueue<>(Collections.reverseOrder());
		int answer =0;
		for(int i=0; i<M+1; i++) {
			int aMove = Integer.parseInt(AmoveInfo[i]);
			int bMove = Integer.parseInt(BmoveInfo[i]);
			
			move(userA, userA.y, userA.x, aMove);
			move(userB, userB.y, userB.x, bMove);
			
			calDistance(userA.y, userA.x, userB.y, userB.x);

			answer+=maxPower.poll();
			answer+=maxPower.poll();
				
			
			maxPower.clear();
			
		}
		System.out.println("#"+test_case+" "+answer);

		}
	}
    	static void calDistance(int ay, int ax, int by, int bx) throws CloneNotSupportedException {

		int maxA=0, maxB=0;
		for(Bc bc: bcList) {
			int adist = Math.abs(ay-bc.X)+ Math.abs(ax-bc.Y);
			int bdist = Math.abs(by-bc.X)+ Math.abs(bx-bc.Y);
			
			if(adist<=bc.C && bdist>bc.C) {
				maxA = Math.max(maxA, bc.P);
			}
			else if(adist>bc.C && bdist<=bc.C) {
				maxB = Math.max(maxB, bc.P);
			}
			else if(adist<=bc.C && bdist<=bc.C) {
				maxPower.add(bc.P);
			}
			
		}
		maxPower.add(maxA);
		maxPower.add(maxB);
	}
	
	
	
	
	static void move(User user, int y, int x, int direction) {
		int ny = y +dy[direction];
		int nx = x +dx[direction];
		
		if(0<=ny && ny<10 && 0<=nx && nx<10) {
			user.y = ny;
			user.x = nx;
		}
		
	}
	
	static class User{
		int x;
		int y;
		
		public User(int x, int y) {
			this.x = x;
			this.y = y;
		}
		
	}
	
	
	static class Bc {
		int X;
		int Y;
		int C;
		int P;

		
		public Bc(){}
		public Bc(int x, int y, int c, int p) {
			X = x;
			Y = y;
			C = c;
			P = p;
		}

	}
}