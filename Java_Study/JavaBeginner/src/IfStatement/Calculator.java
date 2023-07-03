package IfStatement;

import java.util.Scanner;

public class Calculator {

    private int inputValue;
    private int inputNumber1;
    private int inputNumber2;
    final static Scanner scanner = new Scanner(System.in);

    Calculator() {
        System.out.print("Enter Number1: ");
        this.inputNumber1 = scanner.nextInt();

        System.out.print("\nEnter Number2: ");
        this.inputNumber2 = scanner.nextInt();

        printDialog();
        this.inputValue = scanner.nextInt();
    }

    public void printDialog() {
        System.out.println("1 - ADD");
        System.out.println("2 - Subtract");
        System.out.println("3 - Divide");
        System.out.println("4 - Multiply");
    }

    public int calculate() {
        if (this.inputValue == 1) {
            System.out.println("1");
            return this.inputNumber1 + this.inputNumber2;
        } else if (this.inputValue == 2) {
            return this.inputNumber1 - this.inputNumber2;
        } else if (this.inputValue == 3) {
            if (this.inputNumber1 != 0 || this.inputNumber2 != 0) {
                return this.inputNumber1 / this.inputNumber2;
            }
        } else {
            if (this.inputNumber1 != 0 || this.inputNumber2 != 0) {
                return this.inputNumber1 * this.inputNumber2;
            }
        }
        return 0;
    }

    public void calculateSwitch() {
        switch (this.inputValue) {
            case 1:
                 System.out.println(this.inputNumber1 + this.inputNumber2);
                 break;
            case 2:
                System.out.println(this.inputNumber1 - this.inputNumber2);
                break;
            case 3:
                if (this.inputNumber1 != 0 || this.inputNumber2 != 0) {
                    System.out.println(this.inputNumber1 / this.inputNumber2);
                    break;
                }
            case 4:
                if (this.inputNumber1 != 0 || this.inputNumber2 != 0) {
                    System.out.println(this.inputNumber1 * this.inputNumber2);
                    break;
                }
            default:
                System.out.println("Invalid");
        }
    }
}
