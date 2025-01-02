import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        int a=sc.nextInt()-1;
        int b=sc.nextInt()-1;
        sc.close();

        boolean[] visited = new boolean[n];
        for(int i = 0;i<n;i++){
            visited[i]=false;
        }
        visited[a]=true;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{a,0});
        boolean if_solved=false;
        if(a==b){
            System.out.println(0);
            if_solved=true;
        }
        while(!q.isEmpty()){
            if(if_solved){
                break;
            }
            int[] temp = q.poll();
            int start=temp[0];
            int time=temp[1];
            for(int i=start%arr[start];i<n;i+=arr[start]) {
                if (i == b) {
                    System.out.println(time + 1);
                    if_solved = true;
                    break;
                }
                if(!visited[i]){
                    q.add(new int[]{i, time + 1});
                    visited[i]=true;
                }
            }
        }
        if(!if_solved){System.out.println(-1);}
    }
}