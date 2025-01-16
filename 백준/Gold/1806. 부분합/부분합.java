import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int s=sc.nextInt();
        int[] array=new int[n];
        for(int i=0;i<n;i++){
            array[i]=sc.nextInt();
        }
        int a=0;
        int b=1;
        int sum=array[0];
        int answer=n+1;
        while(true){
            if(sum<s){
                //System.out.println("b더하기 "+a+" "+b);
                if(b==n){
                    break;
                }
                sum+=array[b];
                b+=1;
            }
            else{
                //System.out.println("a더하기 "+a+" "+b);
                answer=Math.min(b-a,answer);
                sum-=array[a];
                a+=1;
            }
        }
        if(answer==n+1){System.out.println(0);}
        else{System.out.println(answer);}
    }
}