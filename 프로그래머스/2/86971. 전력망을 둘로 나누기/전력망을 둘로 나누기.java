import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
class Solution {
    private final static Map<Integer,List<Integer>> map=new HashMap<>();
    
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
		
		for(int i=0; i<n; i++) {
			map.put(i+1, new ArrayList<>());
		}
		
		
		
		for(int[] wire : wires) {
			int first = wire[0];
			int second = wire[1];
			
			map.get(first).add(second);
			map.get(second).add(first);
		}
		
		
//		System.out.println(map);
		
		for(int[] wire : wires) {
			int v1 = wire[0];
			int v2 = wire[1];
			
			map.get(v1).remove(Integer.valueOf(v2));
			map.get(v2).remove(Integer.valueOf(v1));
			
			int first = bfs(v1,n);
			int second = bfs(v2,n);
			answer = Integer.min(answer, Math.abs(first-second));
			map.get(v1).add(v2);
			map.get(v2).add(v1);
				
		}
        return answer;
    }
    
    private static int bfs(int start, int n) {
		
		ArrayDeque<Integer> queue = new ArrayDeque<>();
		boolean[] visit = new boolean[n+1];
		visit[start]=true;
		queue.add(start);
		int cnt = 1;
		while(!queue.isEmpty()) {
//			System.out.println(queue);			
			start = queue.pollFirst();
			for(int i: map.get(start)) {
				if(!visit[i]) {
					cnt+=1;
					queue.add(i);
					visit[i]=true;
				}			
			}
		}
		return cnt;	
	}
}