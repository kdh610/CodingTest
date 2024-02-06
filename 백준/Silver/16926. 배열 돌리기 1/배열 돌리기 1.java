import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.security.Timestamp;
import java.util.Arrays;
import java.util.StringTokenizer;

import javax.xml.stream.events.StartDocument;

public class Main {

	public static void main(String[] args) throws Exception{
		
		int[] dy = {1, 0, -1, 0};
		int[] dx = {0, 1, 0, -1};
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		
		int[][] arr = new int[N][M];
		
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int layer = (int)(Math.min(N, M) /2);
		int end=0;
		int ny;
		int nx;
		int tempY;
		int tempX;
		int startY;
		int startX;
		int start;
		
		for(int count=0; count<R; count++) {
			
			for(int i=0; i<layer; i++) {
				tempY = i;
				tempX = i;
				int temp =0;
				for(int j=0; j<4; j++) {
					ny = dy[j];
					nx = dx[j];
					if(j==0) {		//down
						end = N-i;
						startY=i;
						startX=i;
						
					}else if(j==1) { //right
						end = M-i;
						startY=N-1-i;
						startX=i+1;
					}else if(j==2) { //up
						end = N-(i*2);
						startY=N-1-i-1;
						startX=M-1-i;
					}else {			//left
						end = M-(i*2);
						startY=i;
						startX=M-1-i-1;
					}
					
					// down, up
					if(j==0 || j==2) {
						for(int a=startY; j==0?a<end : a>=i; a+=ny) {
							temp = arr[a][startX];
							arr[a][startX] = arr[tempY][tempX];
							arr[tempY][tempX] = temp;
						}
					}else { // right, left
						for(int a=startX; j==1? a<end : a>=i; a+=nx) {
							temp = arr[startY][a];
							arr[startY][a] = arr[tempY][tempX];
							arr[tempY][tempX] = temp;
							
						}
					}
				
					
				}
				
				
			}
		}
		
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
		
		
		
	}

}