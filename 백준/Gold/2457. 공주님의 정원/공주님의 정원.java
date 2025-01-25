import java.io.*;
import java.util.*;

public class Main {
    static int[] months={31,28,31,30,31,30,31,31,30,31,30,31};
    public static int days(String month_, String day_){
        int days=Integer.parseInt(day_);
        for(int i=0;i<Integer.parseInt(month_)-1;i++){
            days+=months[i];
        }
        return days;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        int[][] array=new int[n][2];
        for(int i=0;i<n;i++){
            String[] s=br.readLine().split(" ");
            array[i]=new int[]{days(s[0],s[1]),days(s[2],s[3])};
        }
        //Arrays.sort(array,(a,b) -> Integer.compare(b[1],a[1]));
        Arrays.sort(array,(a,b) -> Integer.compare(a[0],b[0]));
//        for(int i=0;i<n;i++){
//            System.out.print(array[i][0]+" "+array[i][1]);
//            System.out.println();
//        }
        int answer=0;
        int real_end=0;
        int max_end=0;
        int start_point=60;
        for(int i=0;i<n;i++){
            //System.out.print(array[i][0]+" "+array[i][1]+" ");
            if(array[i][0]>start_point){
                if(max_end<array[i][0]){
                    answer=0;
                    break;
                }
                answer++;
                start_point=max_end;
                real_end=max_end;
                if(real_end>=335){
                    break;
                }
            }
            max_end=Math.max(max_end,array[i][1]);
            //System.out.println();
        }
        if(max_end>real_end){
            real_end=max_end;
            answer++;
        }
        if(real_end>=335){
            bw.write(String.valueOf(answer));
        }
        else{
            bw.write("0");
        }
        bw.flush();
        bw.close();
    }
}