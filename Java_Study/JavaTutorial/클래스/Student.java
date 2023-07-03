package 클래스;

public class Student {

//    int studentId;
//    String studentName;
//    String studentAddress;
//
//    public Student() {}
//
//    public Student(int studentId, String studentName, String studentAddress) {
//        this.studentId = studentId;
//        this.studentName = studentName;
//        this.studentAddress = studentAddress;
//    }
//
//    public void showStudentInfo() {
//        System.out.println(studentId + "," + studentName + "," + studentAddress);
//    }
//
//    public String getStduentName() {
//        return this.studentName;
//    }

    private int studentId;
    private String studentName;

    Subject korean;
    Subject math;

    public Student(int id, String name) {
        this.studentId = id;
        this.studentName = name;

        korean = new Subject();
        math = new Subject();
    }

    public void setKoreanSubject(String name, int score) {
        korean.subjectName = name;
        korean.score = score;
    }

    public void setMathSubject(String name, int score) {
        math.subjectName = name;
        math.score = score;
    }

    public void showStudentScore() {
        int total = korean.score + math.score;
        System.out.println(studentName + "학생의 총점은 " + total + "점 입니다.");
    }

    public int getStudentId() {
        return studentId;
    }

    public void setStudentId(int studentId) {
        this.studentId = studentId;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }
}
