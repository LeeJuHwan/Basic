package 반복문;

public class BreakandContinueTest {
//    public static void main(String[] args) {
//
//        int sum = 0;
//        int i;
//
//        for(i = 1; ; i ++){
//
//            sum += i;
//            if(sum > 100){
//                break;
//            }
//
//        }
//        System.out.println(sum);
//        System.out.println(i);
//    }
    public static void main(String[] args) {
        for(int i = 1; i <= 100; i++){
            if(i % 3 != 0){
                continue;
            }
            else {
                System.out.println(i);
            }
        }
    }
}
