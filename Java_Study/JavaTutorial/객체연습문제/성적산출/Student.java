package 객체연습문제.성적산출;

import java.util.ArrayList;

public class Student {

    String name;
    int studentId;
    ArrayList<Subject> subjectList = new ArrayList<>();

    public Student(int studentId, String name) {
        this.name = name;
        this.studentId = studentId;
    }

    public void addSubject(String subjectName, int subjectScore) {
        Subject subject = new Subject();

        subject.setSubject(subjectName);
        subject.setScore(subjectScore);
        subjectList.add(subject);
    }

    public void showStudentInfo() {

        int total = 0;
        for (Subject s : subjectList) {
            total += s.getScore();
            System.out.println("과목 명: " + s.getSubject() + " >> 점수 : " + s.getScore());
        }
        double average = ((double) total / subjectList.size());
        System.out.printf("%s님의 수강 과목은 %d 과목이며, 총 점은 %d 점으로, 평균은 %.1f점 입니다.%n", name,
                subjectList.size(), total, average);


    }
}
