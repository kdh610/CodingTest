import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int[] switchArr = new int[n];
		int i=0;
		while (st.hasMoreElements()) {
			switchArr[i++] = Integer.parseInt(st.nextToken());
		}
		int studentNum = Integer.parseInt(br.readLine());
		
		for(int j=0; j<studentNum; j++) {
			st = new StringTokenizer(br.readLine());
			int gender = Integer.parseInt(st.nextToken());
			int number = Integer.parseInt(st.nextToken());
			
			int left=number-1;
			int right=number+1;
			
			if(gender==1) {
				for(int k=0; k<n; k++) {
					if((k+1)%number==0) {
						switchArr[k]=(switchArr[k]-1)*-1;
					}
				}
			}else {
				
				switchArr[number-1]=(switchArr[number-1]-1)*-1;
				for(int a=0; a<number-1; a++) {
					if((right-1)<n) {
						if(switchArr[left-1]!=switchArr[right-1]) {
							break;
						}
						else {
							
							switchArr[left-1]=(switchArr[left-1]-1)*-1;
							switchArr[right-1]=(switchArr[right-1]-1)*-1;
							left-=1;
							right+=1;
						}
						
					}
					
				}
			}
			
			
			
		}
		
		for(int a=0; a<n; a++) {
            System.out.print(switchArr[a] + " ");
			if((a+1) % 20 == 0)
				System.out.println();
			
		}
		
		
		
		
	}

}