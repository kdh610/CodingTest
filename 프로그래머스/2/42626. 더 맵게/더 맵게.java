import java.util.PriorityQueue;

public class Solution {
	
    public static int solution(int[] scoville, int K) {
        int answer = -1;
        
        
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        for(int i : scoville) {
        	heap.offer(i);
        }
        
        int cnt=0;
        while(true) {
     	    if(heap.size()==1) {
        		if(heap.poll()<K) {
        			cnt=-1;
        		}
        		
        		break;
        	}
        	
        	int first =heap.poll();
        	int second = heap.poll();
        	
        	if(first>=K) {
        		break;
        	}
        	
        	int s = first + (second*2);
        	cnt++;
        	heap.offer(s);
        	
        	
        }
        
        answer = cnt;
        
        return answer;
    }
}