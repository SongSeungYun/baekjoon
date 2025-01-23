import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i=0;i<n;i++){
            pq.offer(Integer.parseInt(br.readLine()));
        }
        int answer=0;
        int temp;
        for(int i=0;i<n-1;i++){
            temp=pq.poll()+pq.poll();
            pq.offer(temp);
            answer+=temp;
        }
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}