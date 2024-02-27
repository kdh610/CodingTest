import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int V,E;
	static ArrayList<ArrayList<int[]>> graph;
	static int[] distance;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		int start = Integer.parseInt(br.readLine());
		distance = new int[V+1];
		
		Arrays.fill(distance, Integer.MAX_VALUE);
		
		graph = new ArrayList<>();
		for(int i=0; i<V+1; i++) {
			graph.add(new ArrayList<int[]>());
		}
		
		for(int i=0; i<E; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			graph.get(a).add(new int[] {b,c});
		}
		
		dijstra(start);
		
		for(int i=1; i<V+1;i++) {
			if(distance[i]==Integer.MAX_VALUE)
				System.out.println("INF");
			else
				System.out.println(distance[i]);
			
		}
		
	}
	
	static void dijstra(int start) {
		
		PriorityQueue<int[]> q = new PriorityQueue<>( (o1,o2) -> o1[0]-o2[0]);
		distance[start] = 0;
		q.add(new int[] {0,start});
		
		while(!q.isEmpty()) {
			
			int[] distNode = q.poll();
			int dist = distNode[0];
			int node = distNode[1];
			
			if( dist>distance[node]) continue;
			
			
			for(int[] next : graph.get(node)) {
				int cost = dist + next[1];
				
				if(cost<distance[next[0]]) {
					distance[next[0]] = cost;
					q.add(new int[] {cost, next[0]});
				}
			}
		}
	}
	
	
	

}