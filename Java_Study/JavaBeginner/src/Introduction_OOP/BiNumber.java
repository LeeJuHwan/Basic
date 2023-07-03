package Introduction_OOP;

public class BiNumber {

    private int numberOne;
    private int numberTwo;

    BiNumber(int numberOne, int numberTwo) {
        this.numberOne = numberOne;
        this.numberTwo = numberTwo;
    }

    public int add() {
        return numberOne + numberTwo;
    }

    public int multiply() {
        return numberOne * numberTwo;
    }

    public void doubleValue() {
        this.numberOne *= 2;
        this.numberTwo *= 2;
    }

    public int getNumberOne() {
        System.out.println(numberOne);
        return numberOne;
    }

    public int getNumberTwo() {
        System.out.println(numberTwo);
        return numberTwo;
    }
}
