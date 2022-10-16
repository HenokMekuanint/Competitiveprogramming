import java.util.*;
public class problem1619A{
public static void main(String[] args){
    Scanner sc= new Scanner(System.in);
    int t =sc.nextInt();
            while(t!=0){
                t--;
                String s = sc.next();
                int count =0;
                int mid=s.length()/2;
                if(s.length()==1) System.out.println("NO");
                else if(s.length()%2 ==0){
                    for(int i=0;i<mid;i++){
                        if(s.charAt(i)==s.charAt(mid+i)){
                            count++;
                        }
                    }
                    if (count==mid) System.out.println("YES");
                    else System.out.println("NO");
                }else System.out.println("NO");
            }
 
}
 
 
        }
