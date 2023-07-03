import java.time.LocalDate;
import java.time.LocalDateTime;

public class Main {

    public static void main(String[] args) {
        LocalDate today = LocalDate.now();
        LocalDateTime now = LocalDateTime.now();

        System.out.println(today.getDayOfWeek());
        System.out.println(now.getSecond());


    }
}