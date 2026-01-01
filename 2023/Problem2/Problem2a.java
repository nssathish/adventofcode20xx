package Problem2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

import static Problem2.Solution.*;

public class Problem2a {
    public static int solve() throws FileNotFoundException {
        var inputScanner = Solution.getScanner ( "input/problem2/problem2.txt" );
        var gameSum = 0;
        for (int gameIteration = 1; inputScanner.hasNextLine (); gameIteration++) {
            var draws = Solution.splitToDraws( inputScanner.nextLine () );
            if (isValidDraws ( draws )) {
                System.out.println(gameIteration);
                gameSum += gameIteration;
            }
        }

        return gameSum;
    }


    private static boolean isValidDraws(String[] draws) {
        for (var draw : draws) {
            var outcomes = Solution.getOutcomes(draw);
            if (isOutcomeOutOfBounds ( outcomes ))
                return false;
        }

        return true;
    }
    private static boolean isOutcomeOutOfBounds(String[] outcomes) {
        for (var outcome: outcomes) {
            outcome = outcome.trim ();
            String[] picks = Solution.getPicks ( outcome );
            var color = picks[1];
            var count = Integer.parseInt ( picks[0] );
            if (isValidGame ( color, count ))
                return true;
        }

        return false;
    }

    private static boolean isValidGame(String color, int count) {
        return getRedCubes ( color, count ) > 12 ||
                getGreenCubes ( color, count ) > 13 ||
                getBlueCubes ( color, count ) > 14;
    }
}
