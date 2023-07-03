// 나이에 따른 요금 책정 if - elif - else문
package 제어문;

import java.util.Scanner;

public class IfElseCondition {
    public static void main(String[] args) {
        int age;
        int charge;

        Scanner scanner = new Scanner(System.in);
        System.out.printf("나이를 입력 하세요 :");
        age = scanner.nextInt();

        if (age < 8) {
            charge = 1000;
            System.out.println("미취학 아동입니다.");
        } else if (age < 14) {
            charge = 2000;
            System.out.println("초등학생 입니다.");
        } else if (age < 20) {
            charge = 2500;
            System.out.println("청소년 입니다.");
        } else {
            charge = 3000;
            System.out.println("성인 입니다.");
        }
        System.out.printf("입장료는 %d원 입니다.",charge);
    }


}
