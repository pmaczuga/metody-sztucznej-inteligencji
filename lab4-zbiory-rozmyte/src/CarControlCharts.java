import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.FunctionBlock;
import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;
import net.sourceforge.jFuzzyLogic.rule.Variable;

public class CarControlCharts
{
    public static void main(String[] args) throws Exception
    {
        try
        {
            String fileName = args[0];
            int speed = Integer.parseInt(args[1]);
            int acceleration = Integer.parseInt(args[2]);
            int distance = Integer.parseInt(args[3]);
            FIS fis = FIS.load(fileName,true);

            //wyswietl wykresy funkcji fuzyfikacji i defuzyfikacji
            FunctionBlock functionBlock = fis.getFunctionBlock(null);
            JFuzzyChart.get().chart(functionBlock);

            //zadaj wartosci wejsciowe
            functionBlock.setVariable("speed", speed);
            functionBlock.setVariable("acceleration", acceleration);
            functionBlock.setVariable("distance", distance);

            //logika sterownika
            functionBlock.evaluate();

            //graficzna prezentacja wyjscia
            Variable power = functionBlock.getVariable("power");
            JFuzzyChart.get().chart(power, power.getDefuzzifier(), true);

            System.out.println("POWER:" + functionBlock.getVariable("power").getValue());

        } catch (ArrayIndexOutOfBoundsException ex)
        {
            System.out.println("Niepoprawna liczba parametrow. Przyklad: java CarControlCharts string<plik_fcl> int<speed> int<acceleration> int<distance>");
        } catch (NumberFormatException ex)
        {
            System.out.println("Niepoprawny parametr. Przyklad: java CarControlCharts string<plik_fcl> int<speed> int<acceleration> int<distance>");
        } catch (Exception ex)
        {
            System.out.println(ex.toString());
        }
    }
}
