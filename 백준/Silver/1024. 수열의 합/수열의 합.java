import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n=scanner.nextInt();
        int l=scanner.nextInt();
        scanner.close();
        boolean if_solved=false;
        for (int i=l;i<101;i++){
            if(i%2==0){
                int temp=n/i-i/2+1;
                if((2*n)%i==0 && (2*n/i)%2==1 && temp>=0){
                    for (int j=temp;j<temp+i;j++){
                        System.out.print(j);
                        System.out.print(" ");
                    }
                    if_solved=true;
                    break;
                }
            }
            else{
                int temp=n/i-i/2;
                if(n%i==0 && temp>=0){
                    for (int j=temp;j<temp+i;j++){
                        System.out.print(j);
                        System.out.print(" ");
                    }
                    if_solved=true;
                    break;
                }
            }
        }
        if(!if_solved){System.out.print(-1);}
    }
}