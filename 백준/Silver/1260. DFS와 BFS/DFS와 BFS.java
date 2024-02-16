import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M, V;
	static ArrayList<Integer>[] graph;
	static StringBuilder sb;
	static boolean[] visit;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		V = Integer.parseInt(st.nextToken());
		graph = new ArrayList[N+1];
		
		for(int i=0; i<N+1;i++) {
			graph[i] = new ArrayList<Integer>();
		}
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			graph[s].add(e);
			graph[e].add(s);
		}	
		
		for(int i=0; i<N+1;i++) {
			Collections.sort(graph[i]);
		}
		
		
		visit = new boolean[N+1];
		sb = new StringBuilder();
		dfs(V);
		System.out.println(sb);
		
		bfs(V);
		System.out.println(sb);
		
	}
	
	static void dfs(int start) {
		if(visit[start]) {
			return;
		}
		
		visit[start] = true;
		sb.append(start+" ");
		
		for(Integer n: graph[start]) {
			dfs(n);
		}
	}
	
	static void bfs(int start) {
		Queue<Integer> Q = new ArrayDeque<Integer>();
		sb = new StringBuilder();
		Q.add(start);
		boolean[] visit = new boolean[N+1];
		visit[start] = true;
		sb.append(start+" ");
		
		while(!Q.isEmpty()) {
			int node = Q.poll();
			for(Integer n  :graph[node]) {
				if(!visit[n]) {
					Q.add(n);
					visit[n]=true;
					sb.append(n+" ");
				}
				
			}
		}
	}
	
	

}