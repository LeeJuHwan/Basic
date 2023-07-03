package 클래스;

public class Students {

    private String studentName;
    private int grade;
    private int money;

    public Students(String studentName, int money) {
        this.studentName = studentName;
        this.money = money;
    }

    public void takeBus(Bus bus) {
        bus.take(1000);
        this.money -= 1000;
    }

    public void takeSubway(Subway subway) {
        subway.take(1200);
        this.money -= 1200;
    }

    public void showStudentInfo() {
        System.out.println(studentName + "님의 남은 돈은 " + money + "원 입니다.");
    }
}
