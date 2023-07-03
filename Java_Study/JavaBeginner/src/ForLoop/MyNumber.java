package ForLoop;

public class MyNumber {

    private int number;

    MyNumber(int number) {
        this.number = number;
    }

    public boolean isPrime() {
        int cnt = 0;

        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
//                cnt += 1;
                return false;
            }

        }
//        if (cnt == 0) {
//            return true;
//        }
        return true;
    }

    public int sumUptoN() {
        int sum = 0;
        for (int i = 0; i <= number; i++) {
            sum += i;
        }
        return sum;
    }

    public int sumOfDivisors() {
        int sum = 0;
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                sum += i;
            }
        }
        return sum;
    }

    public void printANumberTriangle() {
        String str = "";
        for (int i = 1; i <= number; i++) {
            str += i;
            System.out.println(str);
        }
    }
}
