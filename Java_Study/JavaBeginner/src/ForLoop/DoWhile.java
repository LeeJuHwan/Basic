package ForLoop;

import java.util.Scanner;

public class DoWhile {

    private static final Scanner SCANNER = new Scanner(System.in);

    public int printInput() {

        System.out.printf("Enter Numbers : ");
        return SCANNER.nextInt();
    }

    public void cubesValue(int value) {
        if (value > 0) {
            int result = (int) Math.pow(value, 3);
            System.out.println("Cube is " + result);
        }
    }

    public void loop() {
        int value = 1;
        do {
            value = printInput();
            cubesValue(value);
        }
        while(value > 0) ; {
            System.out.println("Thank you Have Fun!");
        }


    }



}
