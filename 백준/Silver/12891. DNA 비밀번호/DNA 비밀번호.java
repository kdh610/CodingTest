import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int s = Integer.parseInt(st.nextToken());
		int p = Integer.parseInt(st.nextToken());
		
		String DNA = br.readLine();
		st = new StringTokenizer(br.readLine());
		
		int A = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		int G = Integer.parseInt(st.nextToken());
		int T = Integer.parseInt(st.nextToken());

		
		int start=0;
		int end = p-1;
		int answer =0;
		
		HashMap<Character, Integer> dnaCounter = new HashMap<>();
		dnaCounter.put('A', 0);
		dnaCounter.put('C', 0);
		dnaCounter.put('G', 0);
		dnaCounter.put('T', 0);
		
		
		for(int i=start; i<=end; i++) {
			dnaCounter.put(DNA.charAt(i), dnaCounter.get(DNA.charAt(i))+1);
		}
		
		
		if(dnaCounter.get('A')>=A && dnaCounter.get('C')>=C && dnaCounter.get('G')>=G && dnaCounter.get('T')>=T) {
			answer++;
		}
		
		while(end<s-1) {
			end++;
			dnaCounter.put(DNA.charAt(end), dnaCounter.get(DNA.charAt(end))+1);
			
			dnaCounter.put(DNA.charAt(start), dnaCounter.get(DNA.charAt(start))-1);
			start++;
			
			
			if(dnaCounter.get('A')>=A && dnaCounter.get('C')>=C && dnaCounter.get('G')>=G && dnaCounter.get('T')>=T) {
				answer++;
			}
		}
		
		
		System.out.println(answer);
		
		
	}

}