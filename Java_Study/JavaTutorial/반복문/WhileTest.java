// 반복문 내에서 덧셈 과정
package 반복문;

public class WhileTest {
    public static void main(String[] args) {
        int num = 1;
        int sum = 0;

        while (num <= 10) {
            sum += num;
            num ++;
        }
        System.out.println(sum);
        System.out.println(num);
    }
}
