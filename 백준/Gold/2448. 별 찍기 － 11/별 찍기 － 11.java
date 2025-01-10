import java.util.Scanner;

public class Main {
    static char[][] array;
    static int n,m;
    public static void recur(int x, int y,int garo, int sero){//x,y,가로,세로 길이
        if(sero==3){
            return;
        }
        for(int i=2;i<garo/4+2;i++){
            array[y-i+1][x-i]='*';
            array[y-i+1][x+i]='*';
        }
        int y_=y-sero/2;
        for(int i=x-garo/4;i<x+garo/4+1;i+=6){
            for(int j=0;j<5;j++){
                array[y_][i+j]='*';
            }
        }
        recur(x-garo/4-1,y,garo/2,sero/2);
        recur(x,y-sero/2,garo/2,sero/2);
        recur(x+garo/4+1,y,garo/2,sero/2);

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m=6*n/3-1;
        array = new char[n][m];
        sc.close();
//        for(int i=0; i<n;i++){
//            for(int j=0;j<m;j++){
//                array[i][j]=' ';
//            }
//        }
        int mid=m/2;
        for(int i=0;i<n;i++){
            array[i][mid-i]='*';
            array[i][mid+i]='*';
        }
        int n_1 = n-1;
        for(int i=0;i<m;i+=6){
            for(int j=0;j<5;j++){
                array[n_1][i+j]='*';
            }
        }
        recur(mid,n_1,m,n);
        StringBuilder answer=new StringBuilder();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(array[i][j]=='*'){
                    answer.append(array[i][j]);
                }
                else{
                    answer.append(' ');
                }
            }
            answer.append("\n");
        }
        System.out.print(answer);
    }
}