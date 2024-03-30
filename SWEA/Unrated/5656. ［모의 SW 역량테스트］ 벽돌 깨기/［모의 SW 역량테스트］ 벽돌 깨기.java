
import java.util.Scanner;
import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class Solution
{
    static int N,W,H;
    static int[][] map;
    static int[][] temp;
    static int[] result;
    static int[] dy = {0,0,1,-1};
    static int[] dx = {1,-1,0,0};
    static int answer = Integer.MAX_VALUE;
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
			answer = Integer.MAX_VALUE;

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        map = new int[H][W];
        result = new int[N];

        for(int i=0; i<H; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<W; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        selectCol(0);
        System.out.println("#"+test_case+" "+answer);

		}
	}
    
      static void selectCol(int cnt) {
        if(cnt==N) {
            //System.out.println("=========="+Arrays.toString(result));

            temp = new int[H][W];
            for(int j=0; j<H; j++) {
                for(int k=0; k<W; k++) {
                    temp[j][k] = map[j][k];
                }
            }
            for(int i=0; i<cnt; i++) {


                breakBrick(result[i], temp);

                int sum=0;
                for(int a=0; a<H; a++) {
                    for(int b=0; b<W; b++) {
                        if(temp[a][b]!=0) sum++;
                    }
                }
                answer = Math.min(answer, sum);
//                System.out.println("ans "+answer);
//                if(result[0]==2 && result[1]==2 && result[2]==7) {
//                    System.exit(0);
//                }

            }
            return;
        }
        for(int i=0; i<W; i++) {
            result[cnt] = i;
            selectCol(cnt+1);
        }
    }

    static void breakBrick(int col, int[][] temp) {
        //System.out.println("col "+col);

        Queue<int[]> Q = new ArrayDeque<int[]>();


        for(int i=0; i<H; i++) {

//            System.out.println("i, col" + i+" "+col);
//            System.out.println(temp[i][col]);

            if(temp[i][col]!=0) {
                Q.add(new int[] {i,col});
                break;
            }
        }

        while(!Q.isEmpty()) {
            int[] yx = Q.poll();
            int y = yx[0];
            int x = yx[1];
            //System.out.println("y,x "+y+" "+x);
            int range = temp[y][x];
           //System.out.println("ragne "+ range);
            temp[y][x]=0;
            for(int i=0; i<4; i++) {
                for(int j=1; j<range; j++) {
                    int ny = y + dy[i]*j;
                    int nx = x + dx[i]*j;
                    //System.out.println("ny,nx "+ny+" "+nx);
                    if(0<=ny && ny<H && 0<=nx && nx<W) {
                        if(temp[ny][nx]!=0) {
                            Q.add(new int[] {ny,nx});
                        }
                    }
                }
            }
        }

//        for(int a=0; a<H; a++) {
//            System.out.println(Arrays.toString(temp[a]));
//        }
//        System.out.println();

        brickDown();
    }


    static void brickDown() {
        Queue<int[]> Q = new ArrayDeque<>();
        for(int i=H-1; i>=0; i--) {
            for(int j=0; j<W; j++) {
                if(temp[i][j]!=0) {
                    Q.add(new int[] {i,j});

                    while(!Q.isEmpty()) {
                        int[] yx = Q.poll();
                        int y = yx[0];
                        int x = yx[1];

                        if(y<H-1 && temp[y+1][x]==0) {
                            temp[y+1][x] = temp[y][x];
                            temp[y][x] =0;
                            Q.add(new int[] {y+1,x});
                        }
                    }
                }
            }
        }

//        System.out.println("블록 다운");
//        for(int a=0; a<H; a++) {
//            System.out.println(Arrays.toString(temp[a]));
//        }
//        System.out.println();

    }
}