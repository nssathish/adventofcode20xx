package Problem1;

import Utilities.AocUtility;

public class Solution {
    public static int _solve(String[] input) {
        int sum = 0;
        for(var str : input) {
            String firstInteger = "";
            String lastInteger = "";
            for(int i = 0; i < str.length (); i++) {
                char ch = str.charAt ( i );
                if (AocUtility.tryParse ( ch )) {
                    if (firstInteger.isBlank ())
                        firstInteger = Character.toString ( ch );
                    else
                        lastInteger = Character.toString ( ch );
                }
            }
            if (lastInteger.isBlank ()) lastInteger = firstInteger;

//            System.out.println ( firstInteger + lastInteger );

            sum += Integer.parseInt (firstInteger + lastInteger);
        }

        return sum;
    }
}
