import java.util.Arrays;
import java.util.PriorityQueue;
class Solution {
    public int solution(String[][] book_time) {
        int cnt = 0;
        
        Arrays.sort(book_time, (o1,o2)-> o1[0].compareTo(o2[0]));
        
        
        System.out.println(Arrays.deepToString(book_time));

        
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        int last = -1;
        
        for(String[] time : book_time) {
        	String start_hour = time[0].split(":")[0];
        	String start_min = time[0].split(":")[1];
        	String end_hour = time[1].split(":")[0];
        	String end_min = time[1].split(":")[1];
        	
        	int start = 60 * Integer.parseInt(start_hour) + Integer.parseInt(start_min);
        	int end = 60 * Integer.parseInt(end_hour) + Integer.parseInt(end_min);
        	
        	if(!heap.isEmpty()) {
        		last = heap.poll();
        		if(last+10<=start) {
        			heap.add(end);
        		}else {
        			heap.add(end);
        			cnt++;
        			heap.add(last);
        		}
        		
        	}else {
        		heap.add(end);
        		cnt++;
        	}
        	
        	
        	
        }
        		
        
        
        
        
        
        
		
        return cnt;
    }
}