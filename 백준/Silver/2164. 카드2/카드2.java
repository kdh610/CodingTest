import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		Queue<Integer> card = new ArrayDeque<Integer>();
		
		for(int i=1; i<=N; i++) {
			card.offer(i);
		}
		
		
		while(card.size()!=1) {
			card.poll();
			
			int first = card.poll();
			card.offer(first);
	
		}
		
		System.out.println(card.poll());
		
		
		
		
		
		
		
	}

}