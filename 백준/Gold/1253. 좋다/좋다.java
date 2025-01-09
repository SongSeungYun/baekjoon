import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] array = new int[n];
        for(int i=0; i<n; i++){
            array[i]=sc.nextInt();
        }
        Arrays.sort(array);
        sc.close();
        int answer=0;
        int a,b;
        for(int i=0;i<n;i++){
            a=0;
            b=n-1;
            if(i==a){a++;}
            if(i==b){b--;}
            while(a<b) {
                if(array[a]+array[b]==array[i]){
                    answer++;
                    break;
                }
                else if(array[a]+array[b]<array[i]){
                    a++;
                    if(a==i){a++;}
                }
                else{
                    b--;
                    if(b==i){b--;}
                }
            }
        }
        System.out.println(answer);
    }
}