import java.math.BigInteger;
import java.util.HashMap;
import java.util.Scanner;
public class Solution{
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        System.out.println(solution(scan.nextLine()));
    }

    public static int solution(String s){
        BigInteger n = new BigInteger(s);
        HashMap<BigInteger,Long> table = new HashMap<BigInteger,Long>();
        table.put(new BigInteger("1"),0L);
        table.put(new BigInteger("2"),1L);
        return (int)fuel(n,table);
    }

    public static long fuel(BigInteger n, HashMap<BigInteger, Long> table){
        if(table.containsKey(n)){
                return table.get(n);
        }
        if(!n.mod(new BigInteger("2")).equals(new BigInteger("0"))){
            table.put(n,Math.min(
                            fuel(n.add(new BigInteger("1")).divide(new BigInteger("2")),table) + 2,
                                    fuel(n.subtract(new BigInteger("1")).divide(new BigInteger("2")),table) + 2));
        }
        else
            table.put(n,fuel(n.divide(new BigInteger("2")),table)+1);
        return table.get(n);
    }
}
