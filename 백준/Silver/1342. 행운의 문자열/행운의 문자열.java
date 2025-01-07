import java.util.ArrayList;
import java.util.Scanner;
import java.util.HashMap;

public class Main {
    static int m;
    static int answer;
    public static void lucky(int n,String s,HashMap<Character,Integer> map){
        if(n==m){
            boolean if_answer=true;
            for(int i=0;i<m-1;i++){
                if(s.charAt(i)==s.charAt(i+1)){
                    if_answer=false;
                    break;
                }
            }
            if(if_answer){
                answer++;
            }
        }
        for(char c:map.keySet()){
            if(map.get(c)==0){
                continue;
            }
            HashMap<Character, Integer> temp_map=new HashMap<>(map);
            temp_map.put(c,temp_map.get(c)-1);
            String temp_s=s+c;
            lucky(n+1,temp_s, temp_map);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        sc.close();

        HashMap<Character,Integer> map=new HashMap<>();
        char[] chars = s.toCharArray();
        for (char c: chars){
            if(!map.containsKey(c)){
                map.put(c,1);
            }
            else{
                map.put(c,map.get(c)+1);
            }
        }
        m=s.length();
        if(m==1){
            System.out.println(1);
        }
        else {
            lucky(0, "", map);
            System.out.println(answer);
        }
    }
}