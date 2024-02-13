
import java.util.Scanner;
import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution
{
    private static int[] kyu; 
	private static int[] in;
	private static int[] result;
	private static boolean[] visit;
	private static int win;
	private static int lose;
    
	public static void main(String args[]) throws Exception
	{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
		int T;
		T=Integer.parseInt(br.readLine());
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{	
            win=0;
            lose=0;
            StringTokenizer st = new StringTokenizer(br.readLine());
			boolean[] select = new boolean[19];
            kyu = new int[9];
            in = new int[9];
            visit = new boolean[9];
            result = new int[9];

            for(int i=0; i<9; i++) {
                int num = Integer.parseInt(st.nextToken());
                kyu[i] = num;
                select[num] = true;
            }
            int index=0;
            for(int i=1; i<19; i++) {
                if(!select[i]) {
                    in[index++]=i;
                }
            }

            perm(0);

            System.out.println("#"+test_case+" "+win+" " + lose);

		}
	}
    
    private static void perm(int cnt) {
		if(cnt==9) {
			if(cardGame(result)) {
				win++;
			}else lose++;
			
			return;
		}
		for(int i=0; i<9; i++) {
			if(!visit[i]) {
				visit[i]=true;
				result[cnt] = in[i];
				perm(cnt+1);
				visit[i]=false;
			}
		}
	}
	
	private static boolean cardGame(int[] inyoung) {
		int kyuScore =0;
		int inScore =0;
		boolean result = true;
		
		
		for(int i=0; i<9; i++) {
			if(kyu[i]>inyoung[i]) {
				kyuScore+=kyu[i]+inyoung[i];
			}else {
				inScore+=kyu[i]+inyoung[i];
			}
		}
		
		if(inScore>kyuScore) {
			result = false;
		}
		return result;
	}
    
    
}