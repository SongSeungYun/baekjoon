import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        boolean[] array=new boolean[1000001];
        for(int i=2;i<1000001;i++){
            array[i]=true;
        }
        for(int i=2;i<1000001;i++){
            if(array[i]){
                for(int j=2*i;j<1000001;j+=i){
                    array[j]=false;
                }
            }
        }
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=3;i<1000001;i++){
            if(array[i]){
                list.add(i);
            }
        }
        Scanner sc = new Scanner(System.in);
        while(true){
            int n=sc.nextInt();
            if (n==0){break;}
            for(Integer i:list){
                if(array[n-i]){
                    System.out.println(n+" = "+i+" + "+(n-i));
                    break;
                }
            }
        }
        sc.close();
    }
}