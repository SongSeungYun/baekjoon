import java.io.*;
import java.util.*;

public class Main {
    public static int color(int n, int k){
        if(k==1){
            return n;
        }
        if(n<4){
            return 0;
        }
        int[][] dp=new int[n+1][k+1];
        for(int i=0;i<=n;i++){
            dp[i][0]=1;
            dp[i][1]=i;
        }
        for(int i=1;i<=k;i++){
            dp[0][i]=0;
        }
        for(int i=1;i<=n;i++){
            for(int j=2;j<=k;j++){
                if(i>2*j-2){
                    dp[i][j]=(dp[i-2][j-1]+dp[i-1][j])%1000000003;
                }
                else{
                    dp[i][j]=0;
                }
            }
        }
//        for(int i=0;i<=k;i++){
//            for(int j=0;j<=n;j++){
//                System.out.print(dp[j][i]+" ");
//            }
//            System.out.println();
//        }
        return (dp[n][k]-dp[n-4][k-2]+1000000003)%1000000003;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        int k=Integer.parseInt(br.readLine());
        bw.write(color(n,k)+"");
        bw.flush();
        bw.close();
    }
}