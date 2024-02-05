
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;
class Top { 
    int index; 
    int height; 
 
    Top(int index, int height) {
        this.index = index;
        this.height = height;
    }
}

public class Main {

	
	public static void main(String[] args)throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
 
        Stack<Top> stack = new Stack<>();
        StringBuilder answer = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        int[] top = new int[N];
        for(int i=0; i<N; i++) {
        	top[i] = Integer.parseInt(st.nextToken());
        }
        
        
        for(int i=0; i<N; i++) {
        	
        	if(stack.isEmpty()) {
        		answer.append(0+" ");
        		stack.add(new Top(i+1, top[i]));
        		continue;
        	}
        	while(true) {
        		if(stack.isEmpty()) {
        			answer.append(0+" ");
        			stack.add(new Top(i+1, top[i]));
        			break;
        		}
        		if(stack.peek().height <= top[i]) {
        			stack.pop();
        			
        		}else {
        			answer.append(stack.peek().index+" ");
        			stack.add(new Top(i+1, top[i]));
        			break;
        		}
        		
        	}
        		
        }
        
        System.out.println(answer);
        
	}

}
