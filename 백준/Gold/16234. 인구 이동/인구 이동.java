import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;

public class Main {
    static int n,l,r;
    static int[][] array;
    static boolean[][] visited;
    static int[] dx={1,-1,0,0};
    static int[] dy={0,0,1,-1};
    public static void bfs(int x, int y){
        visited[y][x]=true;
        Queue<int[]> q=new LinkedList<>();
        q.offer(new int[]{x,y});
        int sum=array[y][x];
        int num=1;
        ArrayList<int[]> list=new ArrayList<>();
        list.add(new int[]{x,y});
        while(!q.isEmpty()){
            int[] temp=q.poll();
            list.add(temp);
            for(int i=0;i<4;i++){
                int nx=temp[0]+dx[i];
                int ny=temp[1]+dy[i];
                if(0<=nx && nx<n && 0<=ny && ny<n && !visited[ny][nx]
                        && l<=Math.abs(array[temp[1]][temp[0]]-array[ny][nx])
                        && Math.abs(array[temp[1]][temp[0]]-array[ny][nx])<=r){
                    num++;
                    sum+=array[ny][nx];
                    visited[ny][nx]=true;
                    q.offer(new int[]{nx,ny});
                }
            }
        }
        for(int[] temp:list){
            array[temp[1]][temp[0]]=sum/num;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        l=sc.nextInt();
        r=sc.nextInt();
        array=new int[n][n];
        visited=new boolean[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                array[i][j]=sc.nextInt();
            }
        }
        int answer=0;
        while(true){
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    visited[i][j]=false;
                }
            }
            int yeonhap=0;
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    if(!visited[i][j]){
                        bfs(j,i);
                        yeonhap++;
                    }
                }
            }
            if(yeonhap==n*n){
                break;
            }
            answer++;
        }
        System.out.println(answer);
    }
}