import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        for(int i=0;i<t;i++){
            int n = Integer.parseInt(br.readLine());
            int[][] sawons=new int[n][2];
            for(int j=0;j<n;j++){
                String[] s = br.readLine().split(" ");
                sawons[j][0]=Integer.parseInt(s[0]);
                sawons[j][1]=Integer.parseInt(s[1]);
            }
            Arrays.sort(sawons,(a,b) -> Integer.compare(a[0],b[0]));
            int temp=sawons[0][1];
            int answer=1;
            for(int j=1;j<n;j++){
                if(sawons[j][1]<temp){
                    answer++;
                    temp=sawons[j][1];
                }
            }
            bw.write(answer+"\n");
        }
        bw.flush();
        bw.close();
    }
}