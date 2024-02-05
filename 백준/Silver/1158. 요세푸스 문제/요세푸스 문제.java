import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st=new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		
		Queue<Integer> arr = new ArrayDeque<>();
		ArrayList<Integer> answer = new ArrayList<>();
		
		for (int i = 0; i < N; i++) {
			arr.add(i+1);
		}
		
		int cnt = 1;
		while(!arr.isEmpty()) {
			
			for(int i=0; i<K-1; i++) {
				int num = arr.poll();
				arr.add(num);
			}
			
			answer.add(arr.poll());
			
		}
		 

			
		System.out.println(answer.toString().replace("[", "<").replace("]", ">"));

	}

}