import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, X, K;
	static int[] cup;
	
	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		

		
		
		
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			X = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			
			cup = new int[N];
			int curPos = X-1;
			
			for(int i=0; i<K; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				if(a-1==curPos) {

					
					curPos = b-1;
				}
				else if(b-1==curPos) {

					curPos = a-1;
				}
				
				
			}
			curPos+=1;
			System.out.println(curPos);
			
			
			
			
			
			
			
			
		
		
		
		
		
	}

}