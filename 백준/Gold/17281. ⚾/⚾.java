import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] inning;
	static boolean[] visit;
	static ArrayList<Integer> battingOrder;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		inning = new int[N][9];
		visit = new boolean[9];
		battingOrder = new ArrayList<>();
		base = new boolean[4];
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<9; j++) {
				inning[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		perm();
		
		System.out.println(maxScore);
		
	}
	
	
	static void perm() {
		
		if(battingOrder.size()==8) {
			battingOrder.add(3, 0);
			//System.out.println(battingOrder);
			//System.out.println("선공");
			play(0);
//			System.out.println("후공");
//			play(1);
			
			
			
			battingOrder.remove(3);
			return;
		}
		
		for(int i=1; i<9; i++) {
			if(!visit[i]) {
				visit[i] = true;
				battingOrder.add(i);
				perm();
				visit[i] = false;
				battingOrder.remove(battingOrder.size()-1);
			}
		}
		
	}
	
	static boolean[] base;
	static int maxScore=0;
	
	static void play(int order) {
		
		int curBatter = 0;
		int score=0;
		
		// N이닝 게임 진행
		for(int i=0; i<N; i++) {
			//System.out.println(i +"이닝");
			int outCnt=0;

			// 타순으로 타자 치기 
			while(true) {
				//System.out.println("현재 타자 "+curBatter);
				//i번째 이닝의 j번째 타자 결과
				base[0] = true;
				int result =inning[i][battingOrder.get(curBatter)]; 
				//System.out.println("결과 "+result);
				if(result==0) {
					outCnt++;
					if(outCnt==3) {
						base[1] = false;
						base[2] = false;
						base[3] = false;
						curBatter = (curBatter+1)%9;
						break;
					}					
				}else {
					if(base[3]) {
						score++;
						base[3]=false;
					}
					if(base[2]) {
						int next = 2 + result;
						if(next>=4) {
							score++;
						}else {
							base[next]=true;
						}
						base[2] = false;
					}
					if(base[1]) {
						int next = 1 + result;
						if(next>=4) {
							score++;
						}else {
							base[next]=true;
						}
						base[1] = false;
					}
					if(base[0]) {
						int next = 0 + result;
						if(next>=4) {
							score++;
						}else {
							base[next]=true;
						}
						base[0] = false;
					}
					
					
					
				}
				
				
				
				curBatter = (curBatter+1)%9;
				
			}
			
			
			
		}
		
		
		//System.out.println("score "+score);
		maxScore = Math.max(maxScore, score);
		
	}
	
	

}