import java.util.Arrays;

public class Solution {
	
    public int solution(int[][] targets) {
        int answer = 1;
        
        Arrays.sort(targets, (o1,o2)-> o1[1]==o2[1]?o1[0]-o2[0] : o1[1]-o2[1]);
        

        int end = targets[0][1];
        
        for(int i=1; i<targets.length; i++) {
        	int s = targets[i][0];
        	int e = targets[i][1];
        	
        	if(s<end) {
        		continue;
        	}else {
        		answer++;
        		end=e;       		
        	}
        }		
        return answer;
    }
}