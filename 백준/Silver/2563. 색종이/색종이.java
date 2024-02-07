import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		boolean[][] arr = new boolean[100][100];
		int cnt=0;
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			for(int a=y; a<y+10; a++){
				for(int b=x; b<x+10; b++) {
					if(arr[a][b]) {
						continue;
					}
					
					arr[a][b] = arr[a][b]|true;
					if(arr[a][b]) {
						cnt++;
					}
					
				}
				
			}
			
		}
		System.out.println(cnt);
		
		
	}

}
