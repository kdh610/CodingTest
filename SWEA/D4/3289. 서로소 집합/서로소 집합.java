import java.util.Scanner;
import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
    static int n,m;
	static int[] parent;
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
			StringTokenizer st = new StringTokenizer(br.readLine());
			StringBuilder sb = new StringBuilder();
            n=Integer.parseInt(st.nextToken());
            m=Integer.parseInt(st.nextToken());
            parent = new int[n+1];

            makeSet();
            for(int i=0; i<m; i++) {
                st = new StringTokenizer(br.readLine());
                int op = Integer.parseInt(st.nextToken());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                if(op==0) {
                    union(a, b);
                }else {
                    if(findCycle(a, b)) sb.append("1");
                    else sb.append("0");
              }
			
			
		}
		System.out.println("#"+test_case+" "+sb);

		}
	}
    
    static void makeSet() {
		for(int i=1; i<n+1; i++) {
			parent[i] = i;
		}
	}
	
	static int find(int x) {
		if(parent[x]!=x) {
			parent[x] = find(parent[x]);
		}
		return parent[x];
	}
	
	static boolean union(int a, int b) {
		a = find(a);
		b = find(b);
		
		if(a==b) return false;
		parent[b] = a;
		return true;
	}
	
	static boolean findCycle(int a, int b) {
		a = find(a);
		b = find(b);
		
		if(a==b) return true;
		return false;
	}
    
}