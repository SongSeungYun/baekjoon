import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.close();

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {n,0});
        boolean[] visited=new boolean[100001];
        visited[n]=true;
        int[] answer=new int[2];

        while(!q.isEmpty()){
            int[] temp=q.poll();
            int loc = temp[0];
            int time = temp[1];
            visited[loc]=true;
            //System.out.println(loc+" "+time);
            if(loc==k){
                answer[0]=time;
                answer[1]=1;
                break;
            }
            if(loc<=99999 && !visited[loc+1]){q.add(new int[] {loc+1,time+1});}
            if(1<=loc && !visited[loc-1]){q.add(new int[] {loc-1,time+1});}
            if(loc<=50000 && !visited[2*loc]){q.add(new int[] {2*loc,time+1});}
        }
        while(!q.isEmpty()){
            int[] temp=q.poll();
            //System.out.println(temp[0]+" "+temp[1]);
            if(temp[1]!=answer[0]){
                break;
            }
            if(temp[0]==k){
                answer[1]++;
            }
        }
        System.out.println(answer[0]+"\n"+answer[1]);
    }
}