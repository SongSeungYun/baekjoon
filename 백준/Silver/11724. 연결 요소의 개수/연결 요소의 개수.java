import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] graph= new int[n+1][n+1];
        int[] visited= new int[n+1];
        int answer=0;
        for(int i=0;i<m;i++){
            int u=sc.nextInt();
            int v=sc.nextInt();
            graph[u][v]=1;
            graph[v][u]=1;
        }
        sc.close();
        Stack<Integer> stack= new Stack<>();
        for(int i=1;i<n+1;i++){
            if(visited[i]==0){
                answer++;
                visited[i]=1;
                stack.clear();
                stack.push(i);
                while(!stack.empty()){
                    int a=stack.pop();
                    for(int j=1;j<n+1;j++){
                        if(graph[a][j]==1 && visited[j]==0){
                            stack.push(j);
                            visited[j]=1;
                        }
                    }
                }
            }
        }
        System.out.println(answer);
    }
}