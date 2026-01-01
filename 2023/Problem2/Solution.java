package Problem2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static int getRedCubes(String color, int count) {
        if (color.equals ( "red" ))
            return count;

        return Integer.MIN_VALUE;
    }

    public static int getBlueCubes(String color, int count) {
        if (color.equals ( "blue" ))
            return count;

        return Integer.MIN_VALUE;
    }

    public static int getGreenCubes(String color, int count) {
        if (color.equals ( "green" ))
            return count;

        return Integer.MIN_VALUE;
    }

    public static String[] splitToDraws(String game) {
        game = game.replaceAll ( "Game \\d+: ", "" );
        return game.split ( ";" );
    }

    public static String[] getOutcomes(String draw) {
        return Arrays.stream( draw.split ( "," ) )
                .map ( String::trim )
                .toArray ( String[]::new );
    }

    public static String[] getPicks(String outcome) {
        return Arrays
                .stream( outcome.split ( " " ) )
                .map ( String::trim )
                .toArray ( String[]::new );
    }
    public static Scanner getScanner(String path) throws FileNotFoundException {
        return new Scanner ( new File (path) );
    }
}
