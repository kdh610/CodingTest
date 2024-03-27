

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
	
	static int[][] sudoku;
	static ArrayList<int[]> empty;

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		sudoku = new int[9][9];
		empty = new ArrayList<>();
		
		for(int i=0; i<9; i++) {
			char[] row = br.readLine().toCharArray();

			for(int j=0; j<9; j++) {
				sudoku[i][j] = row[j]-'0';
			}
		}
		
		for(int i=0; i<9; i++) {
			for(int j=0; j<9; j++) {
				if(sudoku[i][j] == 0) {
					empty.add(new int[] {i,j});
				}
			}
		}
		
		back(0);
		
		
	}
	
	static void back(int start) {
		
//		for(int i=0; i<9; i++) {
//			System.out.println(Arrays.toString(sudoku[i]));
//		}
//		System.out.println();

		if(start==empty.size()) {
			for(int i=0; i<9; i++) {
				for(int j=0; j<9; j++) {
					System.out.print(sudoku[i][j]);
				}
				System.out.println();
			}
			System.exit(0);;
		}
		
		int y = empty.get(start)[0];
		int x = empty.get(start)[1];
		
		


		for(int k=1; k<10; k++) {
			//System.out.println("k "+k);
			//System.out.println("y "+y + " x"+x);
			if(!isDuplicate(y, x, k)) {
				sudoku[y][x] = k;
				back(start+1);
				
				//System.out.println(y+"============== "+x);
				
				sudoku[y][x]=0;
			}
			
		}
	}
	
	static boolean isDuplicate(int y, int x, int k) {
		int target = k;
		
		for(int i=0; i<9; i++) {
			if(i!=x && sudoku[y][i]==target) {
				//System.out.println("행 중복");
				return true;
			}
			if(i!=y && sudoku[i][x]==target) {
				//System.out.println("열 중복");
				return true;
			}	
		}

		int start_row = 0;
		int start_col = 0;
		
		if(3<=y && y<=5) {
			start_row =3; 
		}else if(6<=y && y<=8) {
			start_row=6;
		}
		if(3<=x && x<=5) {
			start_col =3; 
		}else if(6<=x && x<=8) {
			start_col=6;
		}
		
		for(int i=start_row; i<start_row+3; i++) {

			for(int j=start_col; j<start_col+3; j++) {

				if(i!=y && j!=x && sudoku[i][j]==k) {
					//System.out.println("블록 중복");
					return true;
				}
			}
		}

		return false;
	}

	

}
