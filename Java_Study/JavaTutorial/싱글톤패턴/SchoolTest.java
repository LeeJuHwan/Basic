package 싱글톤패턴;

import java.util.Calendar;

public class SchoolTest {
    public static void main(String[] args) {

        School school = School.getInstance();

        School school2 = School.getInstance();

        System.out.println(school == school2);

        Calendar calendar = Calendar.getInstance();

    }
}
