import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;



public class Main {
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		PriorityQueue<int[]> q = new PriorityQueue<>((a,b)->{
			if(a[0] == b[0]) {
				return a[1] - b[1];
			}
			return a[0] - b[0];
		});
		
		for(int i=0; i<N; i++) {
			int x = Integer.parseInt(br.readLine());
			if(x!=0) {
				q.add(new int[] {Math.abs(x),x});
				
			}else {
				if(q.isEmpty()) {
					System.out.println(0);
				}else {
					System.out.println(q.poll()[1]);
				}
			}
		}
		
		
		
		
	}

}