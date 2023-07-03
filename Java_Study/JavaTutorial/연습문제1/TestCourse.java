package 연습문제1;

import javax.sound.sampled.Line;

public class TestCourse {
    public static void main(String[] args) {
//         연습문제 1 - 짝수 구구단(continue문 사용)
//        System.out.println("#### 짝수 구구단 ####");
//        for(int i = 2; i <= 9; i++){
//            if(i % 2 != 0) continue;
//            for (int j = 1; j <= 9; j++) {
//                System.out.printf("%s X %s = %s\n", i, j, i * j);
//            }
//        }
//         구구단을 단보다 곱하는 수가 작거나 같은 경우까지만 출력하는 프로그램을 만들어 보세요
//        for(int i = 2; i <= 9; i ++) {
//            for(int j = 1; j <= i; j++) {
//                System.out.printf("%s X %s = %s\n", i, j, i * j);
//            }
//        }
//        조건문과 반복문을 활용하여 다이아몬드를 출력해 보세요
        int starCount = 1;
        int LineCount = 9;
        int spaceCount = LineCount / 2;
        for(int l = 0; l < LineCount; l ++) {

            for(int i = 0; i  < spaceCount; i ++) {
                System.out.print(" ");
            }
            for(int j = 0; j < starCount; j ++) {
                System.out.print("*");
            }
            for(int k = 0; k < spaceCount; k ++) {
                System.out.print(" ");
            }

            if(l < LineCount/2) {
                starCount += 2;
                spaceCount -= 1;
            }
            else {
                starCount -= 2;
                spaceCount += 1;
            }
            System.out.println();
        }

    }
}
