package ForLoop;

public class MyNumberRunner {

    public static void main(String[] args) {

        MyNumber myNum = new MyNumber(4);

        System.out.println(myNum.isPrime());
        System.out.println(myNum.sumUptoN());
        System.out.println(myNum.sumOfDivisors());
        myNum.printANumberTriangle();
    }
}
