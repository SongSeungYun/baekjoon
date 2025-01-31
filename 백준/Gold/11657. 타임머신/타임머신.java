import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static ArrayList<int[]> graph=new ArrayList<>();
    static long[] dp;
    public static boolean bellman_ford(int start){
        dp[start]=0;
        int srt,dst,cost;
        long cur_cost;
        for(int i=0; i<n; i++){
            for(int[] abc:graph){
                srt=abc[0];
                dst=abc[1];
                cost=abc[2];
                cur_cost=dp[srt]+cost;
                if(dp[srt]!=Integer.MAX_VALUE && dp[dst]>cur_cost){
                    dp[dst]=cur_cost;
                    if(i==n-1){
                        return false;
                    }
                }
            }
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] temp;
        int a,b,c;
        temp=br.readLine().split(" ");
        n = Integer.parseInt(temp[0]);
        int m = Integer.parseInt(temp[1]);
        for(int i=0; i<m; i++){
            temp=br.readLine().split(" ");
            a=Integer.parseInt(temp[0]);
            b=Integer.parseInt(temp[1]);
            c=Integer.parseInt(temp[2]);
            graph.add(new int[]{a,b,c});
        }
        dp=new long[n+1];
        for(int i=1; i<=n; i++){
            dp[i]=Integer.MAX_VALUE;
        }

        if(bellman_ford(1)){
            for(int i=2; i<=n; i++){
                if(dp[i]==Integer.MAX_VALUE){
                    bw.write("-1\n");
                }
                else{
                    bw.write(dp[i]+"\n");
                }
            }
        }
        else{
            bw.write("-1");
        }
        bw.flush();
        bw.close();
    }
}