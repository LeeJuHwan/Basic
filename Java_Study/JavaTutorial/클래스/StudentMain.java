package 클래스;

public class StudentMain {
    public static void main(String[] args) {

//        Student studentLee = new Student(1, "Lee", "Seoul");
//
//        Student studentKim = new Student(2, "Kim", "New York");
//
//        studentLee.showStudentInfo();
//        studentKim.showStudentInfo();
//
//        System.out.println(studentLee);
//        System.out.println(studentKim);

        Student studentLee = new Student(1, "Lee");
        Student studentKim = new Student(2, "Kim");

        studentLee.setKoreanSubject("국어", 100);
        studentLee.setMathSubject("수학", 95);

        studentKim.setKoreanSubject("국어", 80);
        studentKim.setMathSubject("수학", 99);

        studentLee.showStudentScore();
        studentKim.showStudentScore();

//        System.out.println(studentLee.getStudentId());
        studentKim.setStudentName("James");
        studentKim.showStudentScore();
    }
}
