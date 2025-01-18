import java.io.*;
import java.util.*;

public class Main {
    static int n,k,w;
    static Stack<int[]> stack;
    static ArrayList<Integer>[] graph;
    static int[] time,dp;
    static boolean[] visited;
    public static int dfs(int loc){
        if(graph[loc].isEmpty()){
            return time[loc];
        }
        if(visited[loc]){
            return dp[loc];
        }
        visited[loc]=true;
        int temp_max=-1;
        for(int next_loc:graph[loc]){
            temp_max=Math.max(temp_max,dfs(next_loc));
        }
        dp[loc]=time[loc]+temp_max;
        return dp[loc];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t=Integer.parseInt(br.readLine());
        for(int ii=0;ii<t;ii++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            graph = new ArrayList[n+1];
            time=new int[n+1];
            dp=new int[n+1];
            visited=new boolean[n+1];
            st = new StringTokenizer(br.readLine());
            for(int i=1;i<n+1;i++){
                time[i]=Integer.parseInt(st.nextToken());
                dp[i]=-1;
                visited[i]=false;
                graph[i]=new ArrayList<>();
            }
            for(int i=0;i<k;i++){
                st = new StringTokenizer(br.readLine());
                int temp=Integer.parseInt(st.nextToken());
                graph[Integer.parseInt(st.nextToken())].add(temp);
            }
            w = Integer.parseInt(br.readLine());
            bw.write(Integer.toString(dfs(w)));
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
}