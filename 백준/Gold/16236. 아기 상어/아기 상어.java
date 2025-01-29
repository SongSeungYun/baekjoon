import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] array;
    static boolean[][] visited;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,1,-1};
    static int vol=2;
    public static int distance(int x, int y, int[] shark_loc){
        return Math.abs(x-shark_loc[1])+Math.abs(y-shark_loc[0]);
    }
    public static int dfs(int[] start){
        int final_time=0;
        ArrayList<int[]> hubo=new ArrayList<>();
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                visited[i][j]=false;
            }
        }
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{start[0],start[1],0});
        visited[start[0]][start[1]]=true;
        int cur_x,cur_y,cur_time;
        while(!q.isEmpty()){
            int[] temp=q.poll();
            if(array[temp[0]][temp[1]]!=0 && array[temp[0]][temp[1]]<Math.min(vol,7)){
                hubo.add(new int[]{temp[0],temp[1]});
                final_time=temp[2];
                break;
            }
            for(int i=0; i<4; i++){
                cur_x=temp[1]+dx[i];
                cur_y=temp[0]+dy[i];
                cur_time=temp[2];
                if(0<=cur_x && cur_x<n && 0<=cur_y && cur_y<n && !visited[cur_y][cur_x]
                && array[cur_y][cur_x]<=vol){
                    q.offer(new int[]{cur_y,cur_x,cur_time+1});
                    visited[cur_y][cur_x]=true;
                }
            }
        }
        if(final_time==0){
            return 0;
        }
        while(!q.isEmpty() && q.peek()[2]==final_time){
            int[] temp=q.poll();
            if(array[temp[0]][temp[1]]!=0 && array[temp[0]][temp[1]]<vol){
                hubo.add(new int[]{temp[0],temp[1]});
            }
        }
        int min_y=n;
        int min_x=n;
        for(int[] temp:hubo){
            min_y=Math.min(min_y,temp[0]);
        }
        for(int[] temp:hubo){
            if(temp[0]==min_y){
                min_x=Math.min(min_x,temp[1]);
            }
        }
        array[start[0]][start[1]]=0;
        array[min_y][min_x]=9;
        //System.out.print("탐색 과정 : "+min_y+" "+min_x+" "+final_time+"\n");
        return final_time;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n=Integer.parseInt(br.readLine());
        array=new int[n][n];
        visited=new boolean[n][n];
        for(int i=0;i<n;i++){
            String[] s=br.readLine().split(" ");
            for(int j=0;j<n;j++){
                array[i][j]=Integer.parseInt(s[j]);
            }
        }
        int answer=0;
        int eat=0;
        int[] shark_loc=new int[2];//(y좌표, x좌표)
        int[] dest=new int[2];
        while(true){
            //시작점 찾기
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    if(array[i][j]==9){
                        shark_loc=new int[]{i,j};
                    }
                }
            }
            //탐색 시작
            int cur_time=dfs(shark_loc);
            //먹을거 없으면 break
            if(cur_time==0){
                break;
            }
            answer+=cur_time;
            eat++;
            if(eat==vol){
                eat=0;
                vol++;
            }
//            for(int i=0;i<n;i++){
//                for(int j=0;j<n;j++){
//                    System.out.print(array[i][j]+" ");
//                }
//                System.out.println();
//            }
//            System.out.print("탐색 결과 : "+answer+" "+vol+" "+eat+"\n\n");
        }
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}