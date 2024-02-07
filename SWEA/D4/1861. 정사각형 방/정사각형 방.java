
import java.util.Scanner;
import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


class Solution
{
    private static int[] dy = {0,0,1,-1};
	private static int[] dx = {1,-1,0,0};
	private static int N;
	private static int[][] rooms;
    
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T;
		T=Integer.parseInt(br.readLine());
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
            N = Integer.parseInt(br.readLine());

            rooms = new int[N][N];

            for(int i=0; i<N; i++) {
                st = new StringTokenizer(br.readLine());
                for(int j=0; j<N; j++) {
                    rooms[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int max = 0;
            int start = 0;

            for(int i=0; i<N; i++) {
                for(int j=0; j<N; j++) {
                    int result = dfs(i, j, 1);
                    if(result>max) {
                        max = result;
                        start = rooms[i][j];
                    }else if(result==max) {
                        if(start > rooms[i][j]) {
                            start = rooms[i][j];
                        }
                    }
                }
            }

            System.out.println("#"+test_case+" "+start + " " + max);
		}
	}
    	private static int dfs(int y, int x, int cnt) {
		
		
		for(int i=0; i<4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];
			
			if(0<=ny && ny<N && 0<=nx && nx<N) {
				if(rooms[ny][nx] == rooms[y][x]+1) {
					
					cnt = dfs(ny, nx, cnt+1);
				}
				
				
			}
			
		}
		return cnt;
		
	}
    
}