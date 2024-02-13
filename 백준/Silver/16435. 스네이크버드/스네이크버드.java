import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int L = Integer.parseInt(st.nextToken());
		
		int[] heights = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			heights[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(heights);
		
		for (int i : heights) {
			if(i<=L) {
				L++;
			}
			
		}
		
		System.out.println(L);
	}

}