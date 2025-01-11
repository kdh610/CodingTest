import java.util.Arrays;
class Solution {

    
    public long solution(int n, int[] times) {
        long result = 0;
        Arrays.sort(times);
        long left =0, right = (long)n*times[times.length-1];
		
		while(left <= right) {
		
			long mid = (left+right)/2;
			long sum = 0;
			for(int i=0; i <times.length; i++) {
				sum += mid/times[i];
			}
			
			
			if(sum>=n) {
				result = mid;
				right= mid-1;
			}else{
				left = mid+1;
			}
			
		}
		
		
        return result;
    }
}