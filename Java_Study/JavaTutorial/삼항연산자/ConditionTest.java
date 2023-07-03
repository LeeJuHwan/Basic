package 삼항연산자;

import java.util.Scanner;

public class ConditionTest {
    public static void main(String[] args) {
        int max;
        System.out.println("두 수를 입력 받아서 큰 수를 출력 하세요");

        Scanner scanner = new Scanner(System.in);
        System.out.println("입력1 :");
        int x = scanner.nextInt();

        System.out.println("입력2 :");
        int y = scanner.nextInt();

        max = (x>y)? x: y;  // 삼항연산자 -> 자료형 변수 = (조건문)? True value: False value;
        System.out.println(max);
    }
}
