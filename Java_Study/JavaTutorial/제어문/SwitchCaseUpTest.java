// 달력의 날짜를 나타내는 switch-expression ( lambda와 비슷한 유형 )
package 제어문;

import java.util.Scanner;

public class SwitchCaseUpTest {

    public static void main(String[] args) {
        int month;

        Scanner scanner = new Scanner(System.in);
        System.out.println("원하시는 달을 입력하세요.");
        System.out.print("> ");
        month = scanner.nextInt();

        int day = switch(month) {
            case 1, 3, 5, 7, 9, 11 -> {
                yield 31;
            }
            case 2 -> {
                yield 28;
            }
            case 4, 6, 8, 10, 12 -> {
                yield 30;
            }
            default -> {
                System.out.println("잘못 입력 하였습니다.");
                yield 0;
            }
        };
        System.out.printf("%d월은 %d일 까지 있습니다.",month, day);
    }
}
