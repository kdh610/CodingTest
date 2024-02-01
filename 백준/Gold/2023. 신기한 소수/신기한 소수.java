import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static int N;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		
		makeNum(0, 0);
		
	}
	
	
	private static void makeNum(int cnt, int num) {
		if(cnt==N) {
			System.out.println(num);
			return;
		}
		
		for(int i=1; i<10; i++) {
			int next = num*10 +i;
			if(isPrime(next)) {
				
				makeNum(cnt+1,next );
			}
			
		}
		
		
	}
	
	
	
	
	private static boolean isPrime(int x) {
		if(x==1) return false;
		
		for(int i=2; i<(int)Math.sqrt(x)+1; i++) {
			if(x%i==0) {
				return false;
			}
		}
		return true;
	}
	
	
	

}