package 클래스;

public class BirthDayTest {
    public static void main(String[] args) {

        BirthDay day = new BirthDay();
        day.setDay(7);
//        day.setMonth(6);
        day.setMonth(6);
        day.setYear(2023);


        System.out.println(day.isValid());
        System.out.println(day);
        day.printThis();

    }
}
