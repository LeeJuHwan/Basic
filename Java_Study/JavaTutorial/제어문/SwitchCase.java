// 달력의 날짜를 나타내는 switch-case문
package 제어문;

import java.util.Scanner;

public class SwitchCase {

    public static void main(String[] args) {
        int month;
        int day = 0;

        Scanner scanner = new Scanner(System.in);
        System.out.println("원하시는 달을 입력하세요.");
        System.out.print("> ");
        month = scanner.nextInt();

        switch(month) {
            case 1: case 3: case 5: case 7: case 9: case 11:
                day = 31;
                break;
            case 2:
                day = 28;
                break;
            case 4: case 6: case 8: case 10: case 12:
                day = 30;
                break;
            default:
                day = 0;
                System.out.println("잘못 입력 하였습니다.");
                break;
        }
        System.out.printf("%d월은 %d일 까지 있습니다.",month, day);
    }
}
