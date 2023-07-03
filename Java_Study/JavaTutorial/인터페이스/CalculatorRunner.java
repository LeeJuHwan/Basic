package 인터페이스;

public class CalculatorRunner {

    public static void main(String[] args) {

        CompleteCalc calc = new CompleteCalc();

        int num1 = 10;
        int num2 = 2;

        System.out.println(num1 + "+" + num2 + "=" + calc.add(num1, num2));
        System.out.println(num1 + "-" + num2 + "=" + calc.subtract(num1, num2));
        System.out.println(num1 + "/" + num2 + "=" + calc.divide(num1, num2));
        System.out.println(num1 + "*" + num2 + "=" + calc.times(num1, num2));

        calc.showInfo();
    }

}
