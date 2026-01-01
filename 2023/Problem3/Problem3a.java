package Problem3;

import Utilities.AocUtility;

import java.io.FileNotFoundException;
import java.util.regex.Pattern;

public class Problem3a {
    private static final Pattern NumberPattern = Pattern.compile ( "[0-9]" );
    private static final Pattern DotPattern = Pattern.compile ( "\\." );
    public static int solve() throws FileNotFoundException {
        int sum = 0;
        var lines = AocUtility.getInputFromFile ( "input/problem3/problem3a.txt" );
        var previous = "";
        var next = "";

        for(int i = 0; i < lines.length; i++) {
            var current = lines[i];
            if (i + 1 < lines.length) next = lines[i + 1];
            else next = "";
            var chars = current.split ( "" );
            int j = 0;
            while(j < chars.length) {
                if (NumberPattern.matcher ( chars[j] ).matches ()) {
                    var numberBuilder = new StringBuilder (  );
                    var startIndex = j;

                    while (j < chars.length && NumberPattern.matcher ( chars[j] ).matches ( )) {
                        numberBuilder.append ( chars[j++] );
                    }
                    sum += getPartNumber(numberBuilder.toString (), previous, current, next, startIndex, j);
                }
                else j++;
            }
            previous = current;
        }
        return sum;
    }

    private static int getPartNumber(
            String number, String previous, String current, String next,
            int startIndex, int endIndex) {
        if (
                isSpecialCharacterInRange ( current, startIndex, endIndex )
                || (!previous.isBlank () && isSpecialCharacterInRange(previous, startIndex, endIndex))
                || (!next.isBlank () && isSpecialCharacterInRange(next, startIndex, endIndex))
        )
            return Integer.parseInt ( number );

        return 0;
    }

    private static boolean isSpecialCharacterInRange(String line, int startIndex, int endIndex) {
        var containsSpecialCharacterInRange = false;
        for (int i = startIndex; i < endIndex; i++) {
            if (isSpecialCharacter(line.charAt ( i ))) {
                containsSpecialCharacterInRange = true;
                break;
            }
        }
        return containsSpecialCharacterInRange ||
                containsSpecialCharacterNear(line, startIndex - 1, endIndex) ||
                containsSpecialCharacterDiagonally(line, startIndex - 1, endIndex);
    }

    private static boolean containsSpecialCharacterNear(String line, int nearLeft, int nearRight) {
        return (nearLeft >= 0 && isSpecialCharacter ( line.charAt ( nearLeft ) ) ) ||
                (nearRight < line.length () && isSpecialCharacter ( line.charAt ( nearRight ) ));
    }

    private static boolean containsSpecialCharacterDiagonally(String line, int diagonalLeft, int diagonalRight) {
        return (diagonalLeft > 0 && isSpecialCharacter ( line.charAt ( diagonalLeft ) ))
                || (diagonalRight < line.length() && isSpecialCharacter ( line.charAt ( diagonalRight ) ));
    }

    private static boolean isSpecialCharacter(char c) {
        return !NumberPattern.matcher(Character.toString ( c )).matches ()
                && !DotPattern.matcher ( Character.toString ( c ) ).matches ();
    }
}
