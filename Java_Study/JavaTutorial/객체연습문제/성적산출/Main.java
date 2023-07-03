package 객체연습문제.성적산출;

public class Main {

    public static void main(String[] args) {

        Student studentLee = new Student(1001, "Lee");

        studentLee.addSubject("국어", 86);
        studentLee.addSubject("수학", 47);

        Student studentKim = new Student(1002, "Kim");

        studentKim.addSubject("국어", 70);
        studentKim.addSubject("수학", 85);
        studentKim.addSubject("영어", 100);

        studentLee.showStudentInfo();
        System.out.println("======================================");
        studentKim.showStudentInfo();
    }
}
