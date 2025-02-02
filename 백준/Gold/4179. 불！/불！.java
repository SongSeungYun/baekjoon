import java.io.*;
import java.util.*;

public class Main {
    public static int bfs(int sero, int garo, char[][] array){
        Queue<int[]> jihun_q=new LinkedList<>();
        Queue<int[]> bull_q=new LinkedList<>();
        boolean[][] jihun_visited=new boolean[sero][garo];
        boolean[][] bull_visited=new boolean[sero][garo];
        int[] dx={-1,1,0,0};
        int[] dy={0,0,-1,1};
        int[] temp;
        for(int i=0;i<sero;i++){
            for(int j=0;j<garo;j++){
                jihun_visited[i][j]=false;
                bull_visited[i][j]=false;
                if(array[i][j]=='J'){
                    jihun_q.add(new int[]{i,j,0});
                    jihun_visited[i][j]=true;
                }
                else if(array[i][j]=='F'){
                    bull_q.add(new int[]{i,j,0});
                    jihun_visited[i][j]=true;
                    bull_visited[i][j]=true;
                }
            }
        }
        //지훈이 갈 수 있는 곳 계산 -> jihun_visited에 불 경로 추가(n초마다)
        int time=0;
        while(!jihun_q.isEmpty()){
            //System.out.println(time);
            while(!bull_q.isEmpty() && bull_q.peek()[2]==time){
                temp=bull_q.poll();
                for(int i=0;i<4;i++){
                    int x=temp[1]+dx[i];
                    int y=temp[0]+dy[i];
                    int cur_time=temp[2];
                    //System.out.println("불 큐 탐색 : "+x+" "+y+" "+cur_time);
                    if(0<=x && x<garo && 0<=y && y<sero
                            && !bull_visited[y][x] && array[y][x]=='.'){
                        bull_q.offer(new int[]{y,x,cur_time+1});
                        bull_visited[y][x]=true;
                        jihun_visited[y][x]=true;
                    }
                }
            }
            while(!jihun_q.isEmpty() && jihun_q.peek()[2]==time){
                temp=jihun_q.poll();
                for(int i=0;i<4;i++){
                    int x=temp[1]+dx[i];
                    int y=temp[0]+dy[i];
                    int cur_time=temp[2];
                    //System.out.println("지훈 큐 탐색 : "+x+" "+y+" "+cur_time);
                    if(x<0 || x>=garo || y<0 || y>=sero){//좌표 넘으면 탈출
                        return cur_time+1;
                    }
                    if(!jihun_visited[y][x] && array[y][x]=='.'){
                        jihun_q.offer(new int[]{y,x,cur_time+1});
                        jihun_visited[y][x]=true;
                    }
                }
            }

            time++;
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] temp;
        temp=br.readLine().split(" ");
        int r=Integer.parseInt(temp[0]);
        int c=Integer.parseInt(temp[1]);
        char[][] array=new char[r][c];
        for(int i=0;i<r;i++){
            temp=br.readLine().split("");
            for(int j=0;j<c;j++){
                array[i][j]=temp[j].charAt(0);
            }
        }
        int answer=bfs(r,c,array);
        if(answer==-1){
            bw.write("IMPOSSIBLE");
        }
        else{
            bw.write(String.valueOf(answer));
        }
        bw.flush();
        bw.close();
    }
}