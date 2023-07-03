package 반복문;

public class NestedLoopTest {
    public static void main(String[] args) {

        int dan;
        int times;

        for(dan=2, times=1; dan <= 9; dan++){
            for(times = 1; times <= 9; times++){
                System.out.printf("%s X %s = %s\n", dan, times, dan*times);
            }

        }
    }
}
