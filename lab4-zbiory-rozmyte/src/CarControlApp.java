import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.plot.JDialogFis;
import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;
import java.util.*;

public class CarControlApp
{
    // Speed of car driving in front of ours
    private static double frontCarSpeed = 40.0;

    public static void main(String[] args) throws Exception
    {
        FIS fis = null;
        try
        {
            String fileName = args[0];
            fis = FIS.load(fileName,true);
        } catch (ArrayIndexOutOfBoundsException e)
        {
            System.out.print("Wrong number of arguments. Example: java CarControlApp <fcl file>");
        }

        JDialogFis jdf = null;
        if (!JFuzzyChart.UseMockClass) jdf = new JDialogFis(fis, 800, 600);

        double speed = 0.0;
        double acceleration = 0.0;
        double distance = 650.0;
        double power = 0.0;


        double prevousTime = System.currentTimeMillis() / 1000.0;
        while(true)
        {
            double thisTime = System.currentTimeMillis() / 1000.0;
            double diff = thisTime - prevousTime;

            acceleration += power / 10;
            if (acceleration > 50.0) acceleration = 50.0;
            if (acceleration < -50.0) acceleration = -50.0;
            distance -= (speed - frontCarSpeed) * diff;
            speed += acceleration * diff;
            if (speed < 0.0) speed = 0.0;
            if (speed == 0.0) acceleration = 0.0;

            fis.getVariable("speed").setValue(speed);
            fis.getVariable("acceleration").setValue(acceleration);
            fis.getVariable("distance").setValue(distance);
            fis.evaluate();

            if (jdf != null) jdf.repaint();
            power = fis.getVariable("power").getValue();
            System.out.println(String.format("Speed: %2.2f\tacc:%2.2f\tdistance:%2.2f\t=> power: %2.2f %%", speed, acceleration, distance, fis.getVariable("power").getValue()));

            Thread.sleep(100);

            prevousTime = thisTime;
        }
    }
}
