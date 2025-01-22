import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[][] suup=new int[n][2];
        for(int i=0;i<n;i++) {
            String[] s = br.readLine().split(" ");
            suup[i][0] = Integer.parseInt(s[0]);
            suup[i][1] = Integer.parseInt(s[1]);
        }
        Arrays.sort(suup,(a,b) -> Integer.compare(a[0],b[0]));
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(suup[0][1]);
        int answer=1;
        for(int i=1;i<n;i++){
            if(suup[i][0]<pq.peek()){
                answer++;
                pq.add(suup[i][1]);
            }
            else{
                pq.remove();
                pq.add(suup[i][1]);
            }
        }
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}