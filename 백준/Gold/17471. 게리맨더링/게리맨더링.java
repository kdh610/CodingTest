import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int[] population;
	static ArrayList<ArrayList<Integer>> graph;
	static ArrayList<Integer> A, B;
	static boolean[] selected;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		population = new int[N+1];
		
		st = new StringTokenizer(br.readLine());
		for(int i=1; i<N+1; i++) {
			population[i] = Integer.parseInt(st.nextToken());
		}
		
		graph= new ArrayList<>();
		for(int i=0; i<N+1; i++) {
			graph.add(new ArrayList<>());
		}
		
		for(int i=1; i<N+1; i++) {
			st = new StringTokenizer(br.readLine());
			int cnt = Integer.parseInt(st.nextToken());
			for(int j=0; j<cnt; j++) {
				int area = Integer.parseInt(st.nextToken());
				graph.get(i).add(area);
				graph.get(area).add(i);
			}
		}
		
		
		
		for(int i=1; i<=(int)(N/2); i++) {
			//System.out.println("======="+i);
			selected = new boolean[N+1];
			comb(0, 1, i);
		}
		
		if(answer==Integer.MAX_VALUE) {
			System.out.println(-1);
		}else System.out.println(answer);
	}
	
	
	static boolean[] visit;
	static int peopleCount;
	static int count;
	static boolean possible;
	static int answer = Integer.MAX_VALUE;
	
	static void comb(int cnt, int start, int targetCnt) {
		if(cnt==targetCnt) {
			A = new ArrayList<>();
			B = new ArrayList<>();
			for(int i=1; i<N+1; i++) {
				if(selected[i]) A.add(i);
				else B.add(i);
			}
			
			visit = new boolean[N+1];
			count =1;
			peopleCount = population[A.get(0)];
			visit[A.get(0)] = true;
			possible = false;
			//System.out.println("A "+A);
			boolean aResult = dfs(A.get(0), A);
			int aCount = peopleCount;
			//System.out.println("result "+aResult);
			//System.out.println("aCount "+aCount);
			
			visit = new boolean[N+1];
			count=1;
			peopleCount = population[B.get(0)];
			visit[B.get(0)] = true;
			possible = false;
			//System.out.println("B "+B);
			boolean bResult = dfs(B.get(0), B);
			int bCount = peopleCount;
			//System.out.println("result "+bResult);
			//System.out.println("bCount "+bCount);
			
			if(aResult&&bResult) {
				answer= Math.min(answer, Math.abs(aCount-bCount));
			}
			
			
			return;
		}
		for(int i=start; i<N+1; i++) {
			selected[i] = true;
			comb(cnt+1, i+1, targetCnt);
			selected[i] = false;
		}
		
	}
	
	static boolean dfs(int start, ArrayList<Integer> area) {
		
		
		if(count == area.size()) {
			possible =true;
			return true;
		}
		
		
		for(int i: graph.get(start)) {
			if(!visit[i] && area.contains(i)) {
				count++;
				//System.out.println("i "+i);
				//System.out.println("cnt "+count);
				visit[i]=true;
				peopleCount+=population[i];
				dfs(i, area);
			}
			
		}
		
		if(possible) return true;
		else return false;
	}
	
	
	

}