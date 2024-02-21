

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
	
	static int L,C;
	static String[] word;
	static String[] mo = {"a","e","i","o","u"};
	static String[] result;
	static boolean[] visit;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		L=Integer.parseInt(st.nextToken());
		C=Integer.parseInt(st.nextToken());
		
		word = new String[C];		
		word = br.readLine().split(" ");
		
		result = new String[L];
		visit = new boolean[L];
		
		Arrays.sort(word);
		
		comb(0, 0);
		

	}
	
	static void comb(int cnt, int start) {
		if(cnt==L) {
			//System.out.println(Arrays.toString(result));
			int moCnt=0;
			int jaCnt=0;
			for(String s: result) {
				if(Arrays.asList(mo).contains(s)) moCnt++;
				else jaCnt++;
				
			}
			
			if(moCnt>=1 && jaCnt>=2) {
				String password =  Arrays.stream(result)
					.collect(Collectors.joining());
				System.out.println(password);
			}
			
			return;
		}
		
		for(int i=start; i<C; i++) {
			result[cnt]=word[i];
			comb(cnt+1, i+1);
			
		}
		
	}
	
	

}
