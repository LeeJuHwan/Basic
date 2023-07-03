package Introduction_OOP;

public class SimpleInterestFormulaRunner {

    public static void main(String[] args) {
        SimpleInterestFormula calculator = new SimpleInterestFormula("4500.00", "7.5");

        System.out.println(calculator.CalculateToValue(5));
    }
}
