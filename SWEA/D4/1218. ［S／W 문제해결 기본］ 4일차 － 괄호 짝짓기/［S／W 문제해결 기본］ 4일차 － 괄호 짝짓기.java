import java.util.Scanner;
import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner sc = new Scanner(System.in);
		int T=10;
		//T=sc.nextInt();
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
		
            int len = Integer.parseInt(br.readLine());
            String str = br.readLine();
            Stack<Character> stack = new Stack<>();
            int answer =1; 
		
		
            for(int i=0; i<str.length(); i++) {
                if(str.charAt(i)=='{' || str.charAt(i)=='[' || str.charAt(i)=='(' || str.charAt(i)=='<' ) {
                    stack.push(str.charAt(i));
                }else {
                    if(str.charAt(i)=='}' && stack.pop()!='{') {
                        answer=0;
                        break;
                    }
                    if(str.charAt(i)==']' && stack.pop()!='[') {
                        answer=0;
                        break;
                    }
                    if(str.charAt(i)==')' && stack.pop()!='(') {
                        answer=0;
                        break;
                    }
                    if(str.charAt(i)=='>' && stack.pop()!='<') {
                        answer=0;
                        break;
                    }
				
				
				}
            }
		
		
			System.out.println("#"+test_case+ " "+answer);

		}
	}
}