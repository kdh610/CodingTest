

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int N,M;
	static ArrayList<ArrayList<Integer>> graph;
	static int[] inCount;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		inCount = new int[N+1];
		graph = new ArrayList<>();
		
		for(int i=0; i<N+1; i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			graph.get(s).add(e);
			inCount[e]+=1;
		}
		
		Queue<Integer> Q = new ArrayDeque<>();
		for(int i=1; i<N+1; i++) {
			if(inCount[i]==0) {
				Q.add(i);
			}
		}
		
		while(!Q.isEmpty()) {
			int start = Q.poll();
			sb.append(start +" ");
			
			for(int i : graph.get(start)) {
				inCount[i]--;
				if(inCount[i]==0) {
					Q.add(i);

				}
			}
		}
		
		System.out.println(sb);
		
		
	}

}
