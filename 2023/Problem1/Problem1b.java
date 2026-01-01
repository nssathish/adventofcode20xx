package Problem1;
import Utilities.AocUtility;

import java.io.FileNotFoundException;

public class Problem1b {
    public static int solve() throws FileNotFoundException {

        return _solve( AocUtility.getInputFromFile ( "input/problem1/problem1.txt" ));
    }
    private static int _solve(String[] input) {
        return Solution._solve ( AocUtility.cleanAnomalies(input) );
    }
}