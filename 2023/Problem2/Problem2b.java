package Problem2;

import java.io.FileNotFoundException;

public class Problem2b {
    public static int solve() throws FileNotFoundException {
        var inputScanner = Solution.getScanner ( "input/problem2/problem2.txt" );
        int gamePower = 0;

        while (inputScanner.hasNextLine ()) {
            var draws = Solution.splitToDraws ( inputScanner.nextLine () );

            var redCubesCount = 1;
            var greenCubesCount = 1;
            var blueCubesCount = 1;
            for (var draw : draws) {
                var outcomes = Solution.getOutcomes ( draw );
                for (var outcome : outcomes) {
                    var picks = Solution.getPicks ( outcome );

                    var color = picks[1];
                    var count = Integer.parseInt ( picks[0] );

                    switch(color) {
                        case "red":
                            if (count > redCubesCount)
                                redCubesCount = count;
                            break;
                        case "green":
                            if (count > greenCubesCount)
                                greenCubesCount = count;
                            break;
                        default:
                            if (count > blueCubesCount)
                                blueCubesCount = count;
                            break;
                    }

                }
            }

            gamePower += (redCubesCount * greenCubesCount * blueCubesCount);
        }

        return gamePower;
    }
}
