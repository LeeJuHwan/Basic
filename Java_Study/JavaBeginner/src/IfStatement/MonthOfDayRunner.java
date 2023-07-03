package IfStatement;

public class MonthOfDayRunner {

    public static void main(String[] args) {

        MonthOfDay mod = new MonthOfDay();

        System.out.println(mod.isWeekday(0));
        System.out.println(mod.determineOfNameMonth(7));

        int j = 1;
        int i = ( j > 1? 1: 0);

        System.out.println(i);

    }
}
