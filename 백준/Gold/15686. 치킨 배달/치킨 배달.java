

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	
	static int N,M;
	static String[][] chickenMap;
	static ArrayList<int []> chickenList, houseList;
	static ArrayList<int []> notCloseList;
	
	
	public static void main(String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		chickenMap = new String[N][N];
		for(int i=0; i<N; i++) {
			chickenMap[i] = br.readLine().split(" ");
		}
		
		houseList = new ArrayList();
		chickenList = new ArrayList();
		notCloseList = new ArrayList<int[]>();
		
		for(int i=0; i<N;i++) {
			for(int j=0; j<N; j++) {
				if(chickenMap[i][j].equals("1") ) {
					houseList.add(new int[] {i,j,0});
				}else if(chickenMap[i][j].equals("2") ) {
					chickenList.add(new int[] {i,j});
				}
			}
		}
		
		comb(0);
		System.out.println(min);
		
	}
	
	static int min = Integer.MAX_VALUE;
	 
	static void comb(int start) {
		if(notCloseList.size()==M) {
			//System.out.println(notCloseList);
			min=Math.min(min,calChickenDist());
			
			return;
		}
		
		for(int i=start; i<chickenList.size(); i++) {
			notCloseList.add(new int[] {chickenList.get(i)[0],chickenList.get(i)[1]});
			comb(i+1);
			notCloseList.remove(notCloseList.size()-1);
		}
	}
	
	
	static int calChickenDist(){

		int sum=0;
		int dist=650;
		for(int[] house : houseList) {
			dist=650;
			for(int[] notClose: notCloseList) {
				int result = Math.abs(house[0]-notClose[0]) + Math.abs(house[1]-notClose[1]);
				dist = Math.min(dist,result);
			}
			
			sum+=dist;
		}
		return sum;
	}
	

}
