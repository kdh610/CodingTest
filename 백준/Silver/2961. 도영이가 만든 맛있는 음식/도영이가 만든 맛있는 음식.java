import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;



public class Main {
	private static int N;
	static boolean[] visit;
	static int[][] ingredients;
	static int answer = 1000000000;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		
		ingredients = new int[N][2];
		visit = new boolean[N];
		
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			ingredients[i][0] = Integer.parseInt(st.nextToken());
			ingredients[i][1] = Integer.parseInt(st.nextToken());
		}
		
		subSet(0);
		System.out.print(answer);
	}
	
	private static void subSet(int cnt) {
		if(cnt==N) {
			int S=1;
			int B=0;
			for (int i = 0; i < N; i++) {
				if(visit[i]) {
					S*=ingredients[i][0];
					B+=ingredients[i][1];
				}
			}

			if(S>0 && B>0 && answer>Math.abs(S-B)) {
				answer=Math.abs(S-B);
			}
			return;
		}
		
		visit[cnt]=true;
		subSet(cnt+1);
		
		visit[cnt]=false;
		subSet(cnt+1);
		
		
	}
	
	

}