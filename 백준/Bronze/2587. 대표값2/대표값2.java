import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] arr = new int[5];
		
		int sum = 0;
		for(int i=0; i<5; i++) {
			int num = Integer.parseInt(br.readLine());
			arr[i] = num;
			sum+=num;
					
		}
		
		Arrays.sort(arr);
		
		System.out.println((int)sum/5);
		System.out.println(arr[2]);
		
		
	}
}