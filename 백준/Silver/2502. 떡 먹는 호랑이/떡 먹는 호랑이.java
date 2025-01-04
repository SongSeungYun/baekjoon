import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int d=sc.nextInt();
        int k=sc.nextInt();
        sc.close();

        int[] a_array = new int[d];
        int[] b_array = new int[d];
        a_array[0]=1;
        a_array[1]=0;
        b_array[0]=0;
        b_array[1]=1;
        for(int i=2;i<d;i++){
            a_array[i]=a_array[i-2]+a_array[i-1];
            b_array[i]=b_array[i-2]+b_array[i-1];
        }
        for(int i=1;i<k;i++){
            int temp=k-i*a_array[d-1];
            if(temp%b_array[d-1]==0){
                System.out.println(i);
                System.out.print(temp/b_array[d-1]);
                break;
            }
        }
    }
}