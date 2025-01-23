import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static Integer[] array;
    public static int max(int a, int b){
        int max_index=a;
        for(int i=a+1;i<Math.min(n,b);i++){
            if(array[i]>array[max_index]){
                max_index=i;
            }
        }
        return max_index;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n=Integer.parseInt(br.readLine());
        String[] ss = br.readLine().split(" ");
        array=new Integer[n];
        for(int i=0;i<n;i++){
            array[i]=Integer.parseInt(ss[i]);
        }
        if(n==1){
            bw.write(ss[0]);
            bw.flush();
            bw.close();
            return;
        }
        //Integer[] max_array=array.clone();
        //Arrays.sort(max_array,Collections.reverseOrder());
        int s=Integer.parseInt(br.readLine());
        int max_index,temp;
        int dest=0;
        while(dest<n && s>0){
            max_index=max(dest,dest+s+1);
//            System.out.println(max_index+" "+dest+" "+s);
            if(max_index==dest){
                dest++;
                continue;
            }
            for(int i=max_index;i>dest;i--){
                temp=array[i];
                array[i]=array[i-1];
                array[i-1]=temp;
            }
            s-=max_index-dest;
            dest++;
        }
//        int index=0;
//        while(s>0){
//            if(array[index]<array[index+1]){
//                temp=array[index];
//                array[index]=array[index+1];
//                array[index+1]=temp;
//                s--;
//            }
//            if(index==n-1){index=0;}
//            else{index++;}
//        }
        for(int i=0;i<n;i++){
            bw.write(array[i]+" ");
        }
        bw.flush();
        bw.close();
    }
}