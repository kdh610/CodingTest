import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
	static int N,M;
	static ArrayList<ArrayList<Integer>> graph;
	static boolean[] visit;
	static int[] result;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		graph = new ArrayList<>();
		visit = new boolean[N];
		result = new int[5];
		
		
		for(int i=0; i<N; i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()); 
			int b = Integer.parseInt(st.nextToken()); 
			
			graph.get(a).add(b);
			graph.get(b).add(a);
		}
		
		for(int i=0; i<N; i++) {
			result[0] =i;
			visit[i]=true;
			dfs(1, i);
			visit[i]=false;
			
			if(answer==1) {
				break;
			} 
		}
		System.out.println(answer);
		
		
	}
	static int answer;
	static void dfs(int cnt, int start) {
		//System.out.println(Arrays.toString(result));
		if(cnt>=5) {
			
			answer=1;
			
			
			return;
		}
		
		for(int i : graph.get(start)) {
			if(!visit[i]) {
				result[cnt] = i;
				visit[i] =true;
				dfs(cnt+1, i);
				visit[i]=false;
				if(answer==1) return;
			}
			
		}
		
		
	}
	

}