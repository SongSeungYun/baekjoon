import java.util.Scanner;

public class Main {
    static int[][] map,dp;
    static int[] dx={1,-1,0,0};
    static int[] dy={0,0,1,-1};
    static int n,m;
    public static int dfs(int x,int y){
        if(x==n-1 && y==m-1){
            return 1;
        }
        if(dp[y][x]!=-1){
            return dp[y][x];
        }
        dp[y][x]=0;
        for(int i=0;i<4;i++){
            int nx=x+dx[i];
            int ny=y+dy[i];
            if(0<=nx && nx<n && 0<=ny && ny<m && map[y][x]>map[ny][nx]){
                dp[y][x]+=dfs(nx,ny);
            }
        }
        return dp[y][x];
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        m=sc.nextInt();
        n=sc.nextInt();
        map=new int[m][n];
        dp=new int[m][n];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                map[i][j]=sc.nextInt();
                dp[i][j]=-1;
            }
        }
        sc.close();
        System.out.println(dfs(0,0));
    }
}