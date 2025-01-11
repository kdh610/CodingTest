
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		ArrayList<Integer> list = new ArrayList();
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			list.add(Integer.parseInt(st.nextToken()));
		}
		
		list.sort(null);
		
		for(Integer i: list) {
			System.out.println(i);
		}
		
		
		
	}
}
